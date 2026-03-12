import matplotlib.pyplot as plt
import numpy as np

angles = [r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$"]
err = [0.111061180781, 1.38040106562, -0.290550652836]
erth = [0.227457786284, -4.35827319509, -6.49592758534]

x = np.arange(len(angles))
w = 0.35

plt.figure()
plt.bar(x - w/2, err, width=w, label=r"$e_{rr}$")
plt.bar(x + w/2, erth, width=w, label=r"$e_{r\theta}$")
plt.xticks(x, angles)
plt.ylabel("Wall strain rate")
plt.title("Mesh C wall strain-rate components")
plt.legend()
plt.grid(True, axis="y")
plt.tight_layout()
plt.savefig("figure_strain_meshC.png", dpi=300)

print("Saved figure_strain_meshC.png")
