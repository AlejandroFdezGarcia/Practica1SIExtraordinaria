import pandas as pd
import sqlite3

conn = sqlite3.connect('Database.db')

df = pd.read_sql_query("SELECT * FROM alertas INNER JOIN dispositivos ON alertas.origin = dispositivos.ip OR alertas.destination = dispositivos.ip", conn)

df['timestamp'] = pd.to_datetime(df['timestamp'])
df_july = df[df['timestamp'].dt.month == 7]
df_august = df[df['timestamp'].dt.month == 8]


df_filtered_july = df_july[df_july['priority'].isin([1, 2, 3])]
df_priority1_july = df_july[df_july['priority'] == 1]
df_priority2_july = df_july[df_july['priority'] == 2]
df_priority3_july = df_july[df_july['priority'] == 3]

df_filtered_august = df_august[df_august['priority'].isin([1, 2, 3])]
df_priority1_august = df_august[df_august['priority'] == 1]
df_priority2_august = df_august[df_august['priority'] == 2]
df_priority3_august = df_august[df_august['priority'] == 3]

df_filtered = df[(df['timestamp'].dt.month.isin([7, 8])) & (df['priority'].isin([1, 2, 3]))]


vulnerabilities_july = df_filtered_july['analisis_vulnerabilidadesdetectadas']
vulnerabilities_priority1_july = df_priority1_july['analisis_vulnerabilidadesdetectadas']
vulnerabilities_priority2_july = df_priority2_july['analisis_vulnerabilidadesdetectadas']
vulnerabilities_priority3_july = df_priority3_july['analisis_vulnerabilidadesdetectadas']

vulnerabilities_august = df_filtered_august['analisis_vulnerabilidadesdetectadas']
vulnerabilities_priority1_august = df_priority1_august['analisis_vulnerabilidadesdetectadas']
vulnerabilities_priority2_august = df_priority2_august['analisis_vulnerabilidadesdetectadas']
vulnerabilities_priority3_august = df_priority3_august['analisis_vulnerabilidadesdetectadas']

vulnerabilities = df_filtered['analisis_vulnerabilidadesdetectadas']

# Vulnerabilidades observadas
num_observations_july = vulnerabilities_july.count()
num_observations_priority1_july = vulnerabilities_priority1_july.count()
num_observations_priority2_july = vulnerabilities_priority2_july.count()
num_observations_priority3_july = vulnerabilities_priority3_july.count()

num_observations_august = vulnerabilities_august.count()
num_observations_priority1_august = vulnerabilities_priority1_august.count()
num_observations_priority2_august = vulnerabilities_priority2_august.count()
num_observations_priority3_august = vulnerabilities_priority3_august.count()

num_observations = vulnerabilities.count()

# Valores ausentes
num_missing_values_july = vulnerabilities_july.isnull().sum()
num_missing_values_priority1_july = vulnerabilities_priority1_july.isnull().sum()
num_missing_values_priority2_july = vulnerabilities_priority2_july.isnull().sum()
num_missing_values_priority3_july = vulnerabilities_priority3_july.isnull().sum()

num_missing_values_august = vulnerabilities_august.isnull().sum()
num_missing_values_priority1_august = vulnerabilities_priority1_august.isnull().sum()
num_missing_values_priority2_august = vulnerabilities_priority2_august.isnull().sum()
num_missing_values_priority3_august = vulnerabilities_priority3_august.isnull().sum()

num_missing_values = vulnerabilities.isnull().sum()

# Moda
mode_july = vulnerabilities_july.mode().values[0]
mode_priority1_july = vulnerabilities_priority1_july.mode().values[0]
mode_priority2_july = vulnerabilities_priority2_july.mode().values[0]
mode_priority3_july = vulnerabilities_priority3_july.mode().values[0]

mode_august = vulnerabilities_august.mode().values[0]
mode_priority1_august = vulnerabilities_priority1_august.mode().values[0]
mode_priority2_august = vulnerabilities_priority2_august.mode().values[0]
mode_priority3_august = vulnerabilities_priority3_august.mode().values[0]

mode = vulnerabilities.mode().values[0]

# Mediana
median_july = vulnerabilities_july.median()
median_priority1_july = vulnerabilities_priority1_july.median()
median_priority2_july = vulnerabilities_priority2_july.median()
median_priority3_july = vulnerabilities_priority3_july.median()

median_august = vulnerabilities_august.median()
median_priority1_august = vulnerabilities_priority1_august.median()
median_priority2_august = vulnerabilities_priority2_august.median()
median_priority3_august = vulnerabilities_priority3_august.median()

median = vulnerabilities.median()

# Cuartil Q1
q1_july = vulnerabilities_july.quantile(0.25)
q1_priority1_july = vulnerabilities_priority1_july.quantile(0.25)
q1_priority2_july = vulnerabilities_priority2_july.quantile(0.25)
q1_priority3_july = vulnerabilities_priority3_july.quantile(0.25)

q1_august = vulnerabilities_august.quantile(0.25)
q1_priority1_august = vulnerabilities_priority1_august.quantile(0.25)
q1_priority2_august = vulnerabilities_priority2_august.quantile(0.25)
q1_priority3_august = vulnerabilities_priority3_august.quantile(0.25)

q1 = vulnerabilities.quantile(0.25)

# Cuartil Q3
q3_july = vulnerabilities_july.quantile(0.75)
q3_priority1_july = vulnerabilities_priority1_july.quantile(0.75)
q3_priority2_july = vulnerabilities_priority2_july.quantile(0.75)
q3_priority3_july = vulnerabilities_priority3_july.quantile(0.75)

q3_august = vulnerabilities_august.quantile(0.75)
q3_priority1_august = vulnerabilities_priority1_august.quantile(0.75)
q3_priority2_august = vulnerabilities_priority2_august.quantile(0.75)
q3_priority3_august = vulnerabilities_priority3_august.quantile(0.75)

q3 = vulnerabilities.quantile(0.75)

# Valores máximos
max_value_july = vulnerabilities_july.max()
max_value_priority1_july = vulnerabilities_priority1_july.max()
max_value_priority2_july = vulnerabilities_priority2_july.max()
max_value_priority3_july = vulnerabilities_priority3_july.max()

max_value_august = vulnerabilities_august.max()
max_value_priority1_august = vulnerabilities_priority1_august.max()
max_value_priority2_august = vulnerabilities_priority2_august.max()
max_value_priority3_august = vulnerabilities_priority3_august.max()

max_value = vulnerabilities.max()

# Valores mínimos
min_value_july = vulnerabilities_july.min()
min_value_priority1_july = vulnerabilities_priority1_july.min()
min_value_priority2_july = vulnerabilities_priority2_july.min()
min_value_priority3_july = vulnerabilities_priority3_july.min()

min_value_august = vulnerabilities_august.min()
min_value_priority1_august = vulnerabilities_priority1_august.min()
min_value_priority2_august = vulnerabilities_priority2_august.min()
min_value_priority3_august = vulnerabilities_priority3_august.min()

min_value = vulnerabilities.min()


print("Número de observaciones totales en julio:", num_observations_july)
print("Número de observaciones de prioridad 1 en julio:", num_observations_priority1_july)
print("Número de observaciones de prioridad 2 en julio:", num_observations_priority2_july)
print("Número de observaciones de prioridad 3 en julio:", num_observations_priority3_july)

print("Número de observaciones totales en agosto:", num_observations_august)
print("Número de observaciones de prioridad 1 en agosto:", num_observations_priority1_august)
print("Número de observaciones de prioridad 2 en agosto:", num_observations_priority2_august)
print("Número de observaciones de prioridad 3 en agosto:", num_observations_priority3_august)

print("Número de observaciones totales:", num_observations)
print("\n")


print("Número de valores ausentes totales en julio:", num_missing_values_july)
print("Número de valores ausentes de prioridad 1 en julio:", num_missing_values_priority1_july)
print("Número de valores ausentes de prioridad 2 en julio:", num_missing_values_priority2_july)
print("Número de valores ausentes de prioridad 3 en julio:", num_missing_values_priority3_july)

print("Número de valores ausentes en agosto:", num_missing_values_august)
print("Número de valores ausentes de prioridad 1 en agosto:", num_missing_values_priority1_july)
print("Número de valores ausentes de prioridad 2 en agosto:", num_missing_values_priority2_august)
print("Número de valores ausentes de prioridad 3 en agosto:", num_missing_values_priority3_august)

print("Número de valores ausentes totales:", num_missing_values)
print("\n")


print("Moda de julio:", mode_july)
print("Moda de julio (prioridad 1):", mode_priority1_july)
print("Moda de julio (prioridad 2):", mode_priority2_july)
print("Moda de julio (prioridad 3):", mode_priority3_july)

print("Moda de agosto:", mode_august)
print("Moda de agosto (prioridad 1):", mode_priority1_august)
print("Moda de agosto (prioridad 2):", mode_priority2_august)
print("Moda de agosto (prioridad 3):", mode_priority3_august)

print("Moda global:", mode)
print("\n")

print("Mediana de julio:", median_july)
print("Mediana de julio (prioridad 1):", median_priority1_july)
print("Mediana de julio (prioridad 2:", median_priority2_july)
print("Mediana de julio (prioridad 3):", median_priority3_july)

print("Mediana de agosto:", median_august)
print("Mediana de agosto (prioridad 1):", median_priority1_august)
print("Mediana de agosto (prioridad 2):", median_priority2_august)
print("Mediana de agosto (prioridad 3):", median_priority3_august)

print("Mediana global:", median)
print("\n")

print("Cuartil Q1 de julio:", q1_july)
print("Cuartil Q1 de julio (prioridad 1):", q1_priority1_july)
print("Cuartil Q1 de julio (prioridad 2):", q1_priority2_july)
print("Cuartil Q1 de julio (prioridad 3):", q1_priority3_july)

print("Cuartil Q1 de agosto:", q1_august)
print("Cuartil Q1 de agosto (prioridad 1):", q1_priority1_august)
print("Cuartil Q1 de agosto (prioridad 2):", q1_priority2_august)
print("Cuartil Q1 de agosto (prioridad 3):", q1_priority3_august)

print("Cuartil Q1 global:", q1)
print("\n")

print("Cuartil Q3 de julio:", q3_july)
print("Cuartil Q3 de julio (prioridad 1):", q3_priority1_july)
print("Cuartil Q3 de julio (prioridad 2):", q3_priority2_july)
print("Cuartil Q3 de julio (prioridad 3):", q3_priority3_july)

print("Cuartil Q3 de agosto:", q3_august)
print("Cuartil Q3 de julio (prioridad 1):", q3_priority1_august)
print("Cuartil Q3 de agosto (prioridad 2):", q3_priority2_august)
print("Cuartil Q3 de agosto (prioridad 3):", q3_priority3_august)

print("Cuartil Q3 global:", q3)
print("\n")

print("Valor máximo de julio:", max_value_july)
print("Valor máximo de julio (prioridad 1):", max_value_priority1_july)
print("Valor máximo de julio (prioridad 2):", max_value_priority2_july)
print("Valor máximo de julio (prioridad 3):", max_value_priority3_july)

print("Valor máximo de agosto:", max_value_august)
print("Valor máximo de agosto (prioridad 1):", max_value_priority1_august)
print("Valor máximo de agosto (prioridad 2):", max_value_priority2_august)
print("Valor máximo de agosto (prioridad 3):", max_value_priority3_august)

print("Valor máximo:", max_value)
print("\n")

print("Valor mínimo de julio:", min_value_july)
print("Valor mínimo de julio (prioridad 1):", min_value_priority1_july)
print("Valor mínimo de julio (prioridad 2):", min_value_priority2_july)
print("Valor mínimo de julio (prioridad 3):", min_value_priority3_july)

print("Valor mínimo de agosto:", min_value_august)
print("Valor mínimo de agosto (prioridad 1):", min_value_priority1_august)
print("Valor mínimo de agosto (prioridad 2):", min_value_priority2_august)
print("Valor mínimo de agosto (prioridad 3):", min_value_priority3_august)

print("Valor mínimo:", min_value)
print("\n")


conn.close()
