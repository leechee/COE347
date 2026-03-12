import numpy as np

data = np.loadtxt('theta90_ur_ut.txt', skiprows=1)

s = data[:,0]
ur = data[:,1]
ut = data[:,2]

h = s[1] - s[0]

err = (-11*ur[0] + 18*ur[1] - 9*ur[2] + 2*ur[3])/(6*h)

r = 0.5 + s[:4]
g = ut[:4] / r
dgdr = (-11*g[0] + 18*g[1] - 9*g[2] + 2*g[3])/(6*h)
erth = (0.5/2.0) * dgdr

print("theta = pi/2")
print("err =", err)
print("erth =", erth)
