import numpy as np
import matplotlib.pyplot as plt

lam = 4.45
l = 23.7
h = 5.0
xi = (1+1/(2*(l/lam)))

theta_deg = np.linspace(-90, 90, 1000)
theta_rad = np.radians(theta_deg)

psi = (np.pi * l / lam) * (xi - np.cos(theta_rad))
f_single_h = np.abs(np.sin(psi) / psi)
f_single_h /= np.max(f_single_h)
f_single_e = f_single_h * np.cos(theta_rad)

f_array = np.abs(np.cos((np.pi * h / lam) * np.sin(theta_rad)))
f_double_h = f_single_h * f_array
f_double_e = f_single_e * f_array

f_double_h /= np.max(f_double_h)
f_double_e /= np.max(f_double_e)

plt.figure(figsize=(10, 7))

plt.plot(theta_deg, f_single_h, label='Однострижнева (Площина H)', color='blue', linewidth=2)
plt.plot(theta_deg, f_single_e, label='Однострижнева (Площина E)', color='cyan', linestyle='--')
plt.plot(theta_deg, f_double_h, label='Двострижнева (Площина H)', color='green', alpha=0.7)
plt.plot(theta_deg, f_double_e, label='Двострижнева (Площина E)', color='lime', linestyle=':', alpha=0.7)

plt.axhline(y=0.707, color='red', linestyle='--', label='Рівень 0.707')

plt.title('Порівняння ДС для варіанту №8')
plt.xlabel('Кут $\\theta$, град')
plt.ylabel('$F(\\theta)$')
plt.legend(loc='upper right')
plt.grid(True)
plt.xlim([-90, 90])
plt.ylim([0, 1.1])

plt.tight_layout()
plt.savefig('Лабораторна_робота_4_Графік.png')
plt.show()