# Circular Cylinder Assignment – Team Run Guide

This document explains how to reproduce the meshes and run the cases.

-------------------------------------------------

Repository Structure

a2_circular_cylinder
│
├ meshA
│  ├ system/blockMeshDict
│  ├ constant/polyMesh
│  └ run scripts
│
├ meshB
│  ├ system/blockMeshDict
│  ├ constant/polyMesh
│  └ run scripts
│
├ figures
│
└ mesh_description.md

-------------------------------------------------

Loading OpenFOAM on Frontera

Before running the case, load the required modules.

module purge
module load intel/19.0.5
module load impi/19.0.5
module load openfoam/7.0

Verify installation:

echo $WM_PROJECT_VERSION

-------------------------------------------------

Mesh Generation

Mesh A:

cd meshA
blockMesh
checkMesh

Mesh B:

cd meshB
blockMesh
checkMesh

Both meshes are verified with checkMesh and are suitable for simulation.

-------------------------------------------------

Mesh Sizes

Mesh A
~10,000 cells

Mesh B
~20,000 cells

-------------------------------------------------

Running the Solver

To run the solver for a case:

cd meshA
simpleFoam

or

cd meshB
pimpleFoam

depending on the simulation configuration.

-------------------------------------------------

Output Files

Important outputs include:

drag coefficient
velocity fields
pressure fields

Figures should be saved in the repository folder:

figures/

-------------------------------------------------

Notes

The front and back boundaries are defined as:

type empty

This ensures the simulation runs as a two dimensional case.
