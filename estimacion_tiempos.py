import numpy as np

# Datos experimentales para calcular n (t vs h) y m (t vs d)
# Datos de t vs h (para un diámetro fijo, por ejemplo, d = 3.34 mm)
h_valor = np.array([36, 46, 53, 58, 63])  
t_valor_h = np.array([22.51, 33.88, 44.67, 55.32, 70.72]) 

# Datos de t vs d (para una altura fija, por ejemplo, h = 36 mm)
d_valor = np.array([3.34, 5.00, 7.00])  # mm
t_valor_d = np.array([22.51, 10.59, 5.57])  # s

# Calcular la pendiente n (dependencia de t con h) usar logaritmo
log_h = np.log10(h_valor)
log_t_h = np.log10(t_valor_h)
n = (log_t_h[-1] - log_t_h[0]) / (log_h[-1] - log_h[0])

# Calcular la pendiente m (dependencia de t con d) usar logaritomo
log_d = np.log10(d_valor)
log_t_d = np.log10(t_valor_d)
m = -(log_t_d[-1] - log_t_d[0]) / (log_d[-1] - log_d[0])

# Mostrar resultados de n y m en la consola
print(f"Pendiente n (t vs h): {n:.4f}")
print(f"Pendiente m (t vs d): {m:.4f}")

# Calcular la constante k usando un punto experimental
h_exp = 36  # mm
d_exp = 3.34  # mm
t_exp = 22.51  # s
k = t_exp / (h_exp**n * d_exp**-m)

# Mostrar el valor de k
print(f"Constante k: {k:.4f}")

# Valores combinando el nuevo diametro 10 y la nueva altura h
targets = [
    (100, 10),
    (63, 10),
    (58, 10),
    (53, 10),
    (46, 10),
    (36, 10),
    (100, 7),
    (100, 5),
    (100, 3.34),
]

# Calcular tiempos estimados para cada par de (h, d)
predicted_times = []
for h_target, d_target in targets:
    t_predicted = k * (h_target**n) * (d_target**-m)
    predicted_times.append((h_target, d_target, t_predicted))

# Mostrar resultados como lista
print("\nResultados de tiempo estimado (lista):")
for h, d, t in predicted_times:
    print(f"- Altura (h): {h} mm, Diámetro (d): {d} mm, Tiempo estimado (t): {t:.4f} s")
