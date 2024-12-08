import numpy as np

# Datos experimentales logarítmicos
# h = altura 
# d = diametro
# t = tiempo
log_h = np.array([1.556302501, 1.662757832, 1.72427587, 1.763427994, 1.799340549])  
log_d = np.array([0.523746467, 0.698970004, 0.84509804])  # log(d)
log_t = np.array([
    [1.352375495, 1.02489596, 0.745855195],
    [1.529943402, 1.189490314, 0.890979597],
    [1.6642658, 1.29907126, 1.036229544],
    [1.751279104, 1.381295623, 1.105510185],
    [1.849542252, 1.425208051, 1.180985581]
]) 
#datos de prueba
d= 7
h= 63

# sum = sumatoria
N = len(log_h) * len(log_d)
sum_log_h = np.sum(np.repeat(log_h, len(log_d)))
sum_log_d = np.sum(np.tile(log_d, len(log_h)))
sum_log_t = np.sum(log_t.flatten())
sum_log_h2 = np.sum(np.repeat(log_h, len(log_d))**2)
sum_log_d2 = np.sum(np.tile(log_d, len(log_h))**2)
sum_log_h_log_t = np.sum(np.repeat(log_h, len(log_d)) * log_t.flatten())
sum_log_d_log_t = np.sum(np.tile(log_d, len(log_h)) * log_t.flatten())

# Prueba resultado sumatorias
print(f"{sum_log_h:.3f}, {sum_log_d:.3f}, {sum_log_t:.3f}, {sum_log_h2:.3f}, {sum_log_d2:.3f}, {sum_log_h_log_t:.3f}, {sum_log_d_log_t:.3f}, {N}")

# Cálculo pendiente m
numerador_m = sum_log_h_log_t - (sum_log_h * sum_log_t) / N
denominador_m = sum_log_h2 - (sum_log_h**2) / N
m_general = numerador_m / denominador_m

# Cálculo pendiente n 
numerador_n = sum_log_d_log_t - (sum_log_d * sum_log_t) / N
denominador_n = sum_log_d2 - (sum_log_d**2) / N
n_general = numerador_n / denominador_n

# Cálculo intercepto k
log_k_general = (sum_log_t - m_general * sum_log_h - n_general * sum_log_d) / N
# Antilogaritmo del resultado k
k_general = 10**log_k_general

#Fórmula general
tiempo = k_general * h**m_general * d**n_general

print (f"Pendiente de h = m: {m_general:.4f}")
print (f"Pendiente de d = n: {n_general:.4f}")
print (f"intercepto k = k: {k_general:.4f}")

print (f"tiempo predicho para diametro de 7 y altura de 63: {tiempo:.2f}")