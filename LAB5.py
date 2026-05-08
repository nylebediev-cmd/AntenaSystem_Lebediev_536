import numpy as np
import matplotlib.pyplot as plt

N = 14
d = 2.0
lam = 3.15
lam_b = 4.0
nu = 1
k = 2 * np.pi / lam

theta_deg = np.linspace(-90, 90, 2000)
theta_rad = np.deg2rad(theta_deg)

F_ih = np.abs(np.cos(np.pi/2 * np.sin(theta_rad)) / np.cos(theta_rad + 1e-9))

psi = 0.5 * (k * d * np.sin(theta_rad) - (2 * np.pi / lam_b) * d + nu * np.pi)
with np.errstate(divide='ignore', invalid='ignore'):
    F_hc = np.abs(np.sin(N * psi) / (N * np.sin(psi)))
F_hc[np.isnan(F_hc)] = 1.0

F_total_H = F_ih * F_hc

idx = np.where(F_total_H >= 0.707)[0]
theta_L, theta_R = theta_deg[idx[0]], theta_deg[idx[-1]]
width_0707 = theta_R - theta_L

F_total_E = np.ones_like(theta_deg) # Спрямованість відсутня

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

ax1.plot(theta_deg, F_total_H, color='blue', label='ДС у площині H')
ax1.axhline(y=0.707, color='red', linestyle='--', label='Рівень 0.707')
ax1.fill_between(theta_deg, 0, F_total_H, where=(theta_deg >= theta_L) & (theta_deg <= theta_R),
                 color='red', alpha=0.2, label=f'Ширина = {width_0707:.1f}°')
ax1.set_title('Площина H (Горизонтальна)')
ax1.set_xlabel('Кут θ, градуси')
ax1.set_ylabel('F(θ)')
ax1.set_xticks(np.arange(-90, 91, 15))
ax1.grid(True, linestyle=':')
ax1.legend()

ax2.plot(theta_deg, F_total_E, color='green', label='ДС у площині E')
ax2.set_title('Площина E (Вертикальна)')
ax2.set_xlabel('Кут θ, градуси')
ax2.set_ylabel('F(θ)')
ax2.set_ylim([0, 1.2])
ax2.set_xticks(np.arange(-90, 91, 15))
ax2.grid(True, linestyle=':')
ax2.legend()

plt.suptitle(f'Діаграми спрямованості ХЩА (Варіант 13, N={N}, λ={lam}см)', fontsize=14)
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('Лабораторна_робота_5_Графік.png')
plt.show()

print(f"Ширина головної пелюстки (H) на рівні 0.707: {width_0707:.2f} град.")