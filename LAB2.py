import numpy as np
import matplotlib.pyplot as plt

#  (Варіант 13)
lambd = 0.037
a = 0.16


theta = np.arange(0.001, np.pi / 2, 0.0001)
degrees = np.degrees(theta)

F1h = []
Fc = []
F_H = []

for t in theta:
    val_F1h = (1 + np.cos(t)) / 2
    F1h.append(val_F1h)

    u_H = (np.pi * a * np.sin(t)) / lambd
    denom = 1 - (2 * a * np.sin(t) / lambd) ** 2

    if abs(denom) < 1e-5:
        val_Fc = np.pi / 4
    else:
        val_Fc = abs(np.cos(u_H) / denom)

    Fc.append(val_Fc)

    F_H.append(val_F1h * val_Fc)

F1h = np.array(F1h)
Fc = np.array(Fc)
F_H = np.array(F_H)

idx_707 = np.argmin(np.abs(F_H - 0.707))
deg_707 = degrees[idx_707]
val_707 = F_H[idx_707]

min_x, min_y = [], []
max_x, max_y = [], []

for i in range(1, len(F_H) - 1):
    if F_H[i] < F_H[i - 1] and F_H[i] < F_H[i + 1]:
        min_x.append(degrees[i])
        min_y.append(F_H[i])
    # Локальні максимуми (бокові пелюстки)
    elif F_H[i] > F_H[i - 1] and F_H[i] > F_H[i + 1]:
        max_x.append(degrees[i])
        max_y.append(F_H[i])



plt.figure(figsize=(12, 7))


plt.plot(degrees, F1h, label=r'$F_{1h}(\theta)$', color='#1f77b4', linewidth=1.2)  # Синя
plt.plot(degrees, Fc, label=r'$F_C(\theta)$', color='#ff7f0e', linewidth=1.2)  # Помаранчева
plt.plot(degrees, F_H, label=r'$F_H(\theta)$', color='#2ca02c', linewidth=1.5)  # Зелена

plt.scatter(deg_707, val_707, color='red', s=50, zorder=5, label='Рівень половинної потужності в площині H')
plt.plot([0, deg_707], [val_707, val_707], color='red', linestyle='--', linewidth=0.8)
plt.plot([deg_707, deg_707], [0, val_707], color='red', linestyle='--', linewidth=0.8)
plt.text(deg_707 + 1.5, val_707 + 0.02, f'(0.707, {deg_707:.2f}°)', fontsize=10)

plt.scatter(max_x, max_y, color='black', s=40, zorder=5, label=r'$\theta_{max}$ H')
plt.scatter(min_x, min_y, color='blue', s=40, zorder=5, label=r'$\theta_{min}$ H')

plt.xlim(0, 90)
plt.ylim(0, 1.05)
plt.xticks(np.arange(0, 91, 2))  # Крок сітки 2 градуси, як на вашому фото
plt.yticks(np.arange(0, 1.1, 0.1))
plt.grid(True, which='major', linestyle='-', alpha=0.6)
plt.grid(True, which='minor', linestyle=':', alpha=0.3)
plt.minorticks_on()

plt.xlabel(r'Кут $\theta^\circ$', fontsize=12)
plt.legend(loc='upper right', fontsize=11)
plt.tight_layout()

plt.show()