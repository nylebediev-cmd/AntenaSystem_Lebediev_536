import numpy as np
import matplotlib.pyplot as plt

 (Варіант 13)
lambd = 0.037
a = 0.16
b = 0.16


theta = np.arange(0.001, np.pi / 2, 0.0001)
degrees = np.degrees(theta)

F1h = []
Fc_H = []
F_H = []
Fc_E = []
F_E = []


for t in theta:
    val_F1h = (1 + np.cos(t)) / 2
    F1h.append(val_F1h)

    u_H = (np.pi * a * np.sin(t)) / lambd
    denom = 1 - (2 * a * np.sin(t) / lambd) ** 2
    if abs(denom) < 1e-5:
        val_Fc_H = np.pi / 4
    else:
        val_Fc_H = abs(np.cos(u_H) / denom)
    Fc_H.append(val_Fc_H)
    F_H.append(val_F1h * val_Fc_H)

    u_E = (np.pi * b * np.sin(t)) / lambd
    val_Fc_E = abs(np.sin(u_E) / u_E)
    Fc_E.append(val_Fc_E)
    F_E.append(val_F1h * val_Fc_E)


F1h = np.array(F1h)
Fc_H = np.array(Fc_H)
F_H = np.array(F_H)
Fc_E = np.array(Fc_E)
F_E = np.array(F_E)


idx_707_H = np.argmin(np.abs(F_H - 0.707))
deg_707_H = degrees[idx_707_H]
val_707_H = F_H[idx_707_H]

idx_707_E = np.argmin(np.abs(F_E - 0.707))
deg_707_E = degrees[idx_707_E]
val_707_E = F_E[idx_707_E]


def find_extremes(F_array):
    min_x, min_y, max_x, max_y = [], [], [], []
    for i in range(1, len(F_array) - 1):
        if F_array[i] < F_array[i - 1] and F_array[i] < F_array[i + 1]:
            min_x.append(degrees[i])
            min_y.append(F_array[i])
        elif F_array[i] > F_array[i - 1] and F_array[i] > F_array[i + 1]:
            max_x.append(degrees[i])
            max_y.append(F_array[i])
    return min_x, min_y, max_x, max_y

min_x_H, min_y_H, max_x_H, max_y_H = find_extremes(F_H)
min_x_E, min_y_E, max_x_E, max_y_E = find_extremes(F_E)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12)) # Два графіки один під одним

ax1.plot(degrees, F1h, label=r'$F_{1h}(\theta)$', color='#1f77b4', linewidth=1.2)
ax1.plot(degrees, Fc_H, label=r'$F_C(\theta)$ (Площина H)', color='#ff7f0e', linewidth=1.2)
ax1.plot(degrees, F_H, label=r'$F_H(\theta)$', color='#2ca02c', linewidth=1.5)

ax1.scatter(deg_707_H, val_707_H, color='red', s=50, zorder=5, label='Рівень половинної потужності')
ax1.plot([0, deg_707_H], [val_707_H, val_707_H], color='red', linestyle='--', linewidth=0.8)
ax1.plot([deg_707_H, deg_707_H], [0, val_707_H], color='red', linestyle='--', linewidth=0.8)
ax1.text(deg_707_H + 1.5, val_707_H + 0.02, f'(0.707, {deg_707_H:.2f}°)\nШГП = {2*deg_707_H:.2f}°', fontsize=10)

ax1.scatter(max_x_H, max_y_H, color='black', s=40, zorder=5, label='Бокові пелюстки')
ax1.scatter(min_x_H, min_y_H, color='blue', s=40, zorder=5, label='Нулі ДС')

ax1.set_xlim(0, 90)
ax1.set_ylim(0, 1.05)
ax1.set_xticks(np.arange(0, 91, 2))
ax1.set_yticks(np.arange(0, 1.1, 0.1))
ax1.grid(True, which='major', linestyle='-', alpha=0.6)
ax1.grid(True, which='minor', linestyle=':', alpha=0.3)
ax1.minorticks_on()
ax1.set_title('Нормована діаграма спрямованості у площині H', fontsize=14)
ax1.set_ylabel(r'Амплітуда', fontsize=12)
ax1.legend(loc='upper right', fontsize=10)

ax2.plot(degrees, F1h, label=r'$F_{1h}(\theta)$', color='#1f77b4', linewidth=1.2)
ax2.plot(degrees, Fc_E, label=r'$F_C(\theta)$ (Площина E)', color='#ff7f0e', linewidth=1.2)
ax2.plot(degrees, F_E, label=r'$F_E(\theta)$', color='#d62728', linewidth=1.5)

ax2.scatter(deg_707_E, val_707_E, color='green', s=50, zorder=5, label='Рівень половинної потужності')
ax2.plot([0, deg_707_E], [val_707_E, val_707_E], color='green', linestyle='--', linewidth=0.8)
ax2.plot([deg_707_E, deg_707_E], [0, val_707_E], color='green', linestyle='--', linewidth=0.8)
ax2.text(deg_707_E + 1.5, val_707_E + 0.02, f'(0.707, {deg_707_E:.2f}°)\nШГП = {2*deg_707_E:.2f}°', fontsize=10)

ax2.scatter(max_x_E, max_y_E, color='black', s=40, zorder=5, label='Бокові пелюстки')
ax2.scatter(min_x_E, min_y_E, color='blue', s=40, zorder=5, label='Нулі ДС')

ax2.set_xlim(0, 90)
ax2.set_ylim(0, 1.05)
ax2.set_xticks(np.arange(0, 91, 2))
ax2.set_yticks(np.arange(0, 1.1, 0.1))
ax2.grid(True, which='major', linestyle='-', alpha=0.6)
ax2.grid(True, which='minor', linestyle=':', alpha=0.3)
ax2.minorticks_on()
ax2.set_title('Нормована діаграма спрямованості у площині E', fontsize=14)
ax2.set_xlabel(r'Кут $\theta^\circ$', fontsize=12)
ax2.set_ylabel(r'Амплітуда', fontsize=12)
ax2.legend(loc='upper right', fontsize=10)

plt.tight_layout()
plt.show()