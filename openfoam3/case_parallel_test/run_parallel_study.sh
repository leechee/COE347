#!/bin/bash
# Parallel performance study for rhoCentralFoam
# Runs P=1,2,4,8,16 and records T(P) = ClockTime / steps

source /opt/openfoam7/etc/bashrc

CASE_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$CASE_DIR"

PROCS="1 2 4 8 16"
RESULTS_FILE="parallel_results.txt"

echo "P,TotalClockTime_s,NumSteps,T_per_step_s" > "$RESULTS_FILE"

# Build mesh once (shared across all runs)
if [ ! -d constant/polyMesh/faces ]; then
    echo "=== Building mesh ==="
    blockMesh > log.blockMesh 2>&1
fi

for P in $PROCS; do
    echo ""
    echo "=============================="
    echo " Running P = $P processors"
    echo "=============================="

    # Clean previous run output (but not mesh or 0/)
    rm -rf processor* log.rhoCentralFoam_P${P}
    # Remove any written time steps except 0
    for d in $(ls -d [0-9]* 2>/dev/null | grep -v '^0$'); do rm -rf "$d"; done

    if [ "$P" -eq 1 ]; then
        # Serial run
        rhoCentralFoam > log.rhoCentralFoam_P${P} 2>&1
    else
        # Update decomposeParDict
        sed -i "s/numberOfSubdomains [0-9]*;/numberOfSubdomains ${P};/" system/decomposeParDict

        # Update hierarchicalCoeffs based on P
        if [ "$P" -eq 2 ]; then
            NXYZ="(2 1 1)"
        elif [ "$P" -eq 4 ]; then
            NXYZ="(2 2 1)"
        elif [ "$P" -eq 8 ]; then
            NXYZ="(4 2 1)"
        elif [ "$P" -eq 16 ]; then
            NXYZ="(4 4 1)"
        fi
        sed -i "/hierarchicalCoeffs/,/}/ s/n.*([0-9 ]*);/n               ${NXYZ};/" system/decomposeParDict

        decomposePar -force > log.decomposePar_P${P} 2>&1
        mpirun -np $P rhoCentralFoam -parallel > log.rhoCentralFoam_P${P} 2>&1
    fi

    # Extract timing from log
    CLOCK=$(grep "ClockTime" log.rhoCentralFoam_P${P} | tail -1 | awk '{print $6}')
    STEPS=$(grep -c "^Time = " log.rhoCentralFoam_P${P} || echo 0)

    if [ -n "$CLOCK" ] && [ "$STEPS" -gt 0 ]; then
        T_PER_STEP=$(python3 -c "print(f'{float('$CLOCK')/$STEPS:.6f}')")
        echo "  ClockTime = ${CLOCK} s,  Steps = ${STEPS},  T(P) = ${T_PER_STEP} s/step"
        echo "${P},${CLOCK},${STEPS},${T_PER_STEP}" >> "$RESULTS_FILE"
    else
        echo "  WARNING: Could not extract timing from log.rhoCentralFoam_P${P}"
        echo "${P},ERROR,ERROR,ERROR" >> "$RESULTS_FILE"
    fi

    # Clean processor dirs to save space
    rm -rf processor*
done

echo ""
echo "=============================="
echo " Results saved to: $RESULTS_FILE"
cat "$RESULTS_FILE"
echo "=============================="
