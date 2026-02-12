import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Data
N = np.array([400, 1600, 6400, 25600])
C = np.array([0.0014, 0.0029, 0.0148, 0.1133])

# Compute log-log linear regression
log_N = np.log10(N)
log_C = np.log10(C)
slope, intercept, r_value, p_value, std_err = stats.linregress(log_N, log_C)

# The slope is alpha
alpha = slope
beta = 10**intercept

print(f"Scaling exponent α = {alpha:.3f}")
print(f"Coefficient β = {beta:.6f}")
print(f"R² = {r_value**2:.6f}")
print(f"Equation: C = {beta:.6f} × N^{alpha:.3f}")

# Create log-log plot
fig, ax = plt.subplots(figsize=(10, 7))

# Plot data points
ax.loglog(N, C, 'bo', markersize=10, label='Simulation data')

# Plot fit line
N_fit = np.logspace(np.log10(400), np.log10(25600), 100)
C_fit = beta * N_fit**alpha
ax.loglog(N_fit, C_fit, 'r--', linewidth=2, label=f'Fit: C = {beta:.6f} × N^{alpha:.3f}')

ax.set_xlabel('N (number of cells)', fontsize=14, fontweight='bold')
ax.set_ylabel('C (wallclock time per step, s/step)', fontsize=14, fontweight='bold')
ax.set_title('Computational Cost Scaling with Grid Refinement', fontsize=16, fontweight='bold')
ax.grid(True, alpha=0.3, which='both')
ax.legend(fontsize=12)

# Add text box with results
textstr = f'α = {alpha:.3f}\nβ = {beta:.6f}\nR² = {r_value**2:.6f}'
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=12,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('log_log_scaling.png', dpi=300, bbox_inches='tight')
print('\n✓ Plot saved as: log_log_scaling.png')
plt.show()