import numpy as np
import matplotlib.pyplot as plt

def load_file(fname):
    return np.loadtxt(fname, skiprows=1)

# Load data
d45 = load_file("theta45_ur_ut.txt")
d90 = load_file("theta90_ur_ut.txt")
d135 = load_file("theta135_ur_ut.txt")

# theta = pi/4
plt.figure()
plt.plot(d45[:,0], d45[:,1], label=r"$u_r$")
plt.plot(d45[:,0], d45[:,2], label=r"$u_\theta$")
plt.xlabel("s")
plt.ylabel("Velocity")
plt.title(r"Mesh C: $u_r$ and $u_\theta$ at $\theta=\pi/4$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("figure_theta45_meshC.png", dpi=300)

# theta = pi/2
plt.figure()
plt.plot(d90[:,0], d90[:,1], label=r"$u_r$")
plt.plot(d90[:,0], d90[:,2], label=r"$u_\theta$")
plt.xlabel("s")
plt.ylabel("Velocity")
plt.title(r"Mesh C: $u_r$ and $u_\theta$ at $\theta=\pi/2$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("figure_theta90_meshC.png", dpi=300)

# theta = 3pi/4
plt.figure()
plt.plot(d135[:,0], d135[:,1], label=r"$u_r$")
plt.plot(d135[:,0], d135[:,2], label=r"$u_\theta$")
plt.xlabel("s")
plt.ylabel("Velocity")
plt.title(r"Mesh C: $u_r$ and $u_\theta$ at $\theta=3\pi/4$")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("figure_theta135_meshC.png", dpi=300)

print("Saved:")
print("  figure_theta45_meshC.png")
print("  figure_theta90_meshC.png")
print("  figure_theta135_meshC.png")
