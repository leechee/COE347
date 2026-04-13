import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

base = Path(".")

meshes = {
    "A": base / "meshA",
    "C": base / "meshC",
    "D": base / "meshD",
}

def load(mesh, name):
    return np.loadtxt(meshes[mesh] / name, skiprows=1)

def plot_angle(angle_file, title, outname):
    fig, ax = plt.subplots(2, 1, figsize=(7, 8), sharex=True)

    for mesh in ["A", "C", "D"]:
        d = load(mesh, angle_file)
        s = d[:, 0]
        ur = d[:, 1]
        uth = d[:, 2]

        ax[0].plot(s, ur, label=f"Mesh {mesh}")
        ax[1].plot(s, uth, label=f"Mesh {mesh}")

    ax[0].set_ylabel(r"$u_r$")
    ax[1].set_ylabel(r"$u_\theta$")
    ax[1].set_xlabel("Distance from wall, s")
    ax[0].set_title(title)
    ax[0].grid(True)
    ax[1].grid(True)
    ax[0].legend()
    fig.tight_layout()
    fig.savefig(outname, dpi=300)

plot_angle("theta45_ur_ut.txt", r"Velocity profiles at $\theta=\pi/4$", "Figure16_theta45.png")
plot_angle("theta90_ur_ut.txt", r"Velocity profiles at $\theta=\pi/2$", "Figure17_theta90.png")
plot_angle("theta135_ur_ut.txt", r"Velocity profiles at $\theta=3\pi/4$", "Figure18_theta135.png")

# Figure 19
delta = {
    "A": 0.0162,
    "C": 0.0063,
    "D": 0.0043,
}

inv_delta = np.array([1/delta["A"], 1/delta["C"], 1/delta["D"]])

err_pi4   = np.array([0.2630, 0.1111, 0.9856])
err_pi2   = np.array([0.2586, 1.3804, 1.1245])
err_3pi4  = np.array([-0.4226, -0.2906, -0.3912])

erth_pi4  = np.array([-0.1785, 0.2275, 0.0000])
erth_pi2  = np.array([-2.5959, -4.3583, -4.0402])
erth_3pi4 = np.array([-2.4722, -6.4959, -7.3796])

fig, ax = plt.subplots(2, 1, figsize=(7, 8), sharex=True)

ax[0].plot(inv_delta, err_pi4, "o-", label=r"$\theta=\pi/4$")
ax[0].plot(inv_delta, err_pi2, "s-", label=r"$\theta=\pi/2$")
ax[0].plot(inv_delta, err_3pi4, "^-", label=r"$\theta=3\pi/4$")
ax[0].set_ylabel(r"$e_{rr}$")
ax[0].set_title(r"Wall strain components vs $1/\delta$")
ax[0].grid(True)
ax[0].legend()

ax[1].plot(inv_delta, erth_pi4, "o-", label=r"$\theta=\pi/4$")
ax[1].plot(inv_delta, erth_pi2, "s-", label=r"$\theta=\pi/2$")
ax[1].plot(inv_delta, erth_3pi4, "^-", label=r"$\theta=3\pi/4$")
ax[1].set_ylabel(r"$e_{r\theta}$")
ax[1].set_xlabel(r"$1/\delta$")
ax[1].grid(True)
ax[1].legend()

fig.tight_layout()
fig.savefig("Figure19_strain_vs_invdelta.png", dpi=300)

print("Saved Figure16_theta45.png")
print("Saved Figure17_theta90.png")
print("Saved Figure18_theta135.png")
print("Saved Figure19_strain_vs_invdelta.png")
