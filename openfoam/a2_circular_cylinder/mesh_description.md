# Computational Domain Schematic

The computational domain represents 2D incompressible flow over a circular cylinder.

Domain dimensions

x direction: -4 to 6  
y direction: -4 to 4  

Cylinder

center: (0, 0)  
radius: 0.5  

Boundary conditions

inlet: uniform velocity inlet  
outlet: zero gradient outlet  
top: symmetryPlane  
bottom: symmetryPlane  
cylinder: no slip wall  
frontAndBack: empty (2D simulation)

ASCII schematic of the domain

        top (symmetryPlane)
        y = 4
        ----------------------------------------
        |                                      |
        |                                      |
inlet   |             O  cylinder              |   outlet
x = -4  |                                      |   x = 6
        |                                      |
        ----------------------------------------
        y = -4
        bottom (symmetryPlane)

The mesh is generated using blockMesh with structured blocks and grading near the cylinder and wake region. Mesh A contains approximately 10^4 cells and Mesh B contains approximately 2×10^4 cells for improved resolution of unsteady vortex shedding.
