import matplotlib.pyplot as plt
import pandas as pd

# Datos iniciales para h = 36 mm
#diametros de h36 en milímetros
diametros_h36 = [3.34, 5, 7]
#tiempos asociados a h=36 respectivo a los 3 diámetros
tiempos_h36 = [22.51, 10.59, 5.57]  

# Valores de -n a probar
n_values = [-1, -2, -3, -4]

# Calcular d^-n para cada n
dn_data = {f"d^{n}": [d ** n for d in diametros_h36] for n in n_values}

# Crear un DataFrame para mostrar los valores de d^-n junto con los diámetros originales
df_dn = pd.DataFrame(dn_data)
df_dn["Diámetros originales"] = diametros_h36
#Reordenamiento de las columnas
df_dn = df_dn[["Diámetros originales"] + list(dn_data.keys())]  

# Mostrar la tabla de resultados en la consola
print("Tabla de valores de d^n para diferentes n:")
print(df_dn)

# Graficar t vs D (d^-n) para cada n
plt.figure(figsize=(12, 8))

for n, dn_values in dn_data.items():
    plt.plot(
        dn_values,
        tiempos_h36,
        marker='o',
        linestyle='-',  
        label=f't vs {n}'
    )

# Etiquetas y título de la gráfica
plt.title("t vs D (d^n) para diferentes valores de n  respecto a (h = 36 mm)", fontsize=14)
plt.xlabel("D (d^n)", fontsize=12)
plt.ylabel("Tiempo (s)", fontsize=12)
plt.legend(loc="upper right", fontsize=10)
plt.grid(True)

plt.tight_layout()
plt.show()
