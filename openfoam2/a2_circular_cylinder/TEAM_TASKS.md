# Circular Cylinder Assignment – Team Task Tracker

This document tracks responsibilities for each team member.

-----------------------------------------------------

Person 1 – Mesh Generation and Case Setup

Completed
- Generated Mesh A (~10k cells)
- Generated Mesh B (~20k cells)
- Verified both meshes using checkMesh
- Fixed frontAndBack boundary to type empty
- Exported mesh verification outputs
- Organized repository structure
- Documented mesh details

Remaining
- Generate mesh screenshots in ParaView
- Save mesh visualization images in figures/
- Confirm meshes run correctly with solver
- Assist with debugging if simulations fail

-----------------------------------------------------

Person 2 – Low Reynolds Simulations

Run steady simulations using Mesh A for:

Re = 10  
Re = 50  
Re = 100  

Tasks
- Run solver
- Extract drag coefficient
- Export velocity contour plots
- Save figures in figures/

-----------------------------------------------------

Person 3 – Higher Reynolds Simulations

Run steady simulations using Mesh A for:

Re = 200  
Re = 500  

Tasks
- Run solver
- Extract drag coefficient
- Export wake velocity plots
- Save figures in figures/

-----------------------------------------------------

Person 4 – Unsteady Simulation

Use Mesh B for the unsteady case.

Tasks
- Run pimpleFoam
- Compute lift and drag history
- Export vortex shedding visualization
- Save figures in figures/

-----------------------------------------------------

Shared Responsibilities

All members should:

- Save plots to figures/
- Document results for the report
- Verify simulations run without errors
