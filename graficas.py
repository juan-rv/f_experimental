import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Datos experimentales
#Diametros en milímetros
diametros = np.array([3.34, 5, 7])
#Álturas en milímetros
alturas = np.array([36, 46, 53, 58, 63])  
#Tiempos en segundos
tiempo = np.array([
    [22.51, 33.88, 46.16, 56.4, 70.72],  # tiempos para diámetro 3.34
    [10.59, 15.47, 19.91, 24.06, 26.62],  # tiempos para diámetro 5
    [5.57, 7.78, 10.87, 12.75, 15.17]    # tiempos para diámetro 7
])  

# Conversión a logaritmo base 10
log_diametros = np.log10(diametros)
log_alturas = np.log10(alturas)
log_tiempo = np.log10(tiempo)


# Graficar t vs d en escala lineal
print("\nVisualizar la gráfica t vs d (escala lineal):")
plt.figure(figsize=(8, 6))
for i, h in enumerate(alturas):
    plt.plot(diametros, tiempo[:, i], marker="o", label=f"h={h} mm")

plt.title("Relación t vs d (escala lineal)")
plt.xlabel("Diámetro [mm]")
plt.ylabel("Tiempo [s]")
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()

# Graficar t vs h en escala lineal
print("\nVisualizar gráfica t vs h (escala lineal):")
plt.figure(figsize=(8, 6))
for i, d in enumerate(diametros):
    plt.plot(alturas, tiempo[i, :], marker="o", label=f"d={d} mm")

plt.title("Relación t vs h (escala lineal)")
plt.xlabel("Altura [mm]")
plt.ylabel("Tiempo [s]")
plt.legend()
plt.grid(True, linestyle="--", linewidth=0.5)
plt.show()

# Graficar t vs d en escala log-log y lista en consola
print("\nResultados y gráfica para logt vs logd (escala log-log):")
plt.figure(figsize=(8, 6))
for i, h in enumerate(alturas):
    popt, _ = curve_fit(lambda d, k, n: k * (d ** n), diametros, tiempo[:, i])
    n = popt[1]
    log_k = np.log10(popt[0])
    k = popt[0]
    #visualizar datos en consola
    print(f"h={h} mm: Pendiente (n) = {n:.4f}, log10(k) = {log_k:.4f}, k = {k:.4f}")
    #formato del gráfico
    plt.plot(log_diametros, log_tiempo[:, i], marker="o", label=f"h={h} mm\nn: {n:.4f}, log(k): {log_k:.4f}")

plt.title("Relación logt vs logd (escala log-log)")
plt.xlabel("log(Diámetro) [mm]")
plt.ylabel("log(Tiempo) [s]")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()

# Graficar t vs h en escala log-log y lista en consola
print("\nResultados y gráfica para logt vs logh (escala log-log):")
plt.figure(figsize=(8, 6))
for i, d in enumerate(diametros):
    popt, _ = curve_fit(lambda h, k, n: k * (h ** n), alturas, tiempo[i, :])
    n = popt[1]
    log_k = np.log10(popt[0])
    k = popt[0]
    
    #visualizar datos en consola
    print(f"d={d} mm: Pendiente (n) = {n:.4f}, log10(k) = {log_k:.4f}, k = {k:.4f}")
    #formato del grafico
    plt.plot(log_alturas, log_tiempo[i, :], marker="o", label=f"d={d} mm\nn: {n:.4f}, log(k): {log_k:.4f}")

plt.title("Relación logt vs logh (escala log-log)")
plt.xlabel("log(Altura) [mm]")
plt.ylabel("log(Tiempo) [s]")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()


