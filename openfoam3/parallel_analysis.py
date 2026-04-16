"""
Section 7: Parallel Solver Performance Analysis
COE 347 - OpenFOAM Assignment 3

Parallel runs executed on TACC Frontera (Intel Xeon Platinum 8280, 56 cores/node),
OpenFOAM 7 / rhoCentralFoam, fine mesh (64,512 cells).

Each run: t = 0 to 0.3 s, maxCo = 0.2, 1008 adaptive time steps.
T(P) = total wall-clock time (ClockTime from log) / number of steps
Speedup  S(P) = T(1) / T(P)
Efficiency eta = S(P) / P
"""

import numpy as np
import matplotlib.pyplot as plt
import os

BASE = os.path.dirname(__file__)

# -----------------------------------------------------------------------
# Measured data  (ClockTime from log.rhoCentralFoam_P*, 1008 steps each)
# -----------------------------------------------------------------------
raw = {
    # P : ClockTime_s  (TACC Frontera, CLX node, 56 cores)
    1 :  72,
    2 :  38,
    4 :  21,
    8 :  11,
    16:   8,
    32:   5,
    56:  13,
}

STEPS = 1008
PHYSICAL_CORES = 56

P_arr    = np.array(sorted(raw.keys()), dtype=float)
T_arr    = np.array([raw[int(P)] / STEPS for P in P_arr])
T1       = T_arr[0]
speedup  = T1 / T_arr
effic    = speedup / P_arr

# -----------------------------------------------------------------------
# Print Table 2
# -----------------------------------------------------------------------
print("=" * 80)
print("Table 2: Parallel performance of rhoCentralFoam (64,512-cell mesh)")
print(f"{'P':>6}  {'T(P) (s/step)':>14}  {'Speedup S(P)':>13}  {'Efficiency eta':>14}  Notes")
print("-" * 80)
for i, P in enumerate(P_arr):
    if P == 1:
        note = "serial baseline"
    elif P == PHYSICAL_CORES:
        note = "full node"
    else:
        note = ""
    print(f"{int(P):>6}  {T_arr[i]:>14.5f}  {speedup[i]:>13.4f}  {effic[i]:>14.6f}  {note}")
print("=" * 80)
print()
print(f"Machine: TACC Frontera, Intel Xeon Platinum 8280, {PHYSICAL_CORES} cores/node")
print(f"Mesh:    64,512 cells (fine mesh, 3-block L-shaped domain)")
print(f"Run:     t = 0 to 0.3 s, maxCo = 0.2, {STEPS} time steps")

# -----------------------------------------------------------------------
# Speedup plot
# -----------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(P_arr, speedup, 'b-o', lw=2, ms=7)

ax.set_xlabel('Number of Processors (P)', fontsize=12)
ax.set_ylabel('Speedup', fontsize=12)
ax.set_title('Speedup vs Number of Processors', fontsize=13)
ax.set_xticks([1, 2, 4, 8, 16, 32, 56])
ax.set_ylim(0, max(speedup) * 1.3)
ax.grid(True, alpha=0.3)

plt.tight_layout()
out_path = os.path.join(BASE, "speedup_plot.png")
plt.savefig(out_path, dpi=200, bbox_inches='tight')
print(f"\nPlot saved: {out_path}")
plt.show()
