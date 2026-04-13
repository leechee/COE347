import numpy as np

data = np.loadtxt('postProcessing/sample/300/centerline_U.xy')

x = data[:,0]
ux = data[:,3]

for i in range(len(ux)-1):
    if ux[i] < 0 and ux[i+1] > 0:
        x1 = x[i]
        x2 = x[i+1]
        u1 = ux[i]
        u2 = ux[i+1]

        xzero = x1 - u1*(x2-x1)/(u2-u1)

        L = xzero - 0.5
        LD = L/1.0

        print("zero crossing x =", xzero)
        print("L =", L)
        print("L/D =", LD)
        break
