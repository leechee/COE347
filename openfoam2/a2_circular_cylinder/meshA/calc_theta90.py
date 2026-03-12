import numpy as np

data = np.loadtxt('postProcessing/sample/200/theta90_U.xy')

x = data[:,0]
y = data[:,1]
ux = data[:,3]
uy = data[:,4]

s = y - 0.5
ur = uy
ut = -ux

out = np.column_stack((s, ur, ut))
np.savetxt('theta90_ur_ut.txt', out, header='s ur utheta', comments='')

print("Saved theta90_ur_ut.txt")
print(out[:10])
