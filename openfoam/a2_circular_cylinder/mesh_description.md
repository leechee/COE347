# Preliminary Meshes for Circular Cylinder

## Mesh A
Mesh A is the coarse preliminary mesh used for the low Reynolds number steady simulation.
The mesh contains 10230 cells and uses a thin 3D domain with front and back boundaries
defined as empty so the flow is solved as two dimensional.

The domain extends from x = -4 to x = 6 and y = -4 to y = 4.

## Mesh B
Mesh B is the refined preliminary mesh used for the unsteady simulation.
The mesh contains 20050 cells and also uses a thin 3D domain with front
and back boundaries defined as empty.

The geometry and grading provide increased resolution in the cylinder
region and wake.

## Included Files
Each mesh directory includes:
- system/blockMeshDict
- blockMesh output
- checkMesh output
- exported boundary file confirming frontAndBack is empty
