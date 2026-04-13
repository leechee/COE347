import numpy as np

data = np.loadtxt('theta45_U.txt')

x = data[:,0]
y = data[:,1]
ux = data[:,3]
uy = data[:,4]

xw = 0.3536
yw = 0.3536

s = np.sqrt((x-xw)**2 + (y-yw)**2)

theta = np.pi/4

ur = ux*np.cos(theta) + uy*np.sin(theta)
ut = -ux*np.sin(theta) + uy*np.cos(theta)

out = np.column_stack((s, ur, ut))
np.savetxt('theta45_ur_ut.txt', out, header='s ur utheta', comments='')

print("Saved theta45_ur_ut.txt")
print(out[:10])
