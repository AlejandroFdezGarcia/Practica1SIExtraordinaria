import pandas as pd
import sqlite3

conn = sqlite3.connect('Database.db')

df = pd.read_sql_query("SELECT * FROM alertas INNER JOIN dispositivos ON alertas.origin = dispositivos.ip OR alertas.destination = dispositivos.ip", conn)

df['timestamp'] = pd.to_datetime(df['timestamp'])

df_filtered = df[(df['timestamp'].dt.month.isin([7, 8])) & (df['priority'].isin([1,2,3]))]

vulnerabilities = df_filtered['analisis_vulnerabilidadesdetectadas']

num_observations = vulnerabilities.count()

num_missing_values = vulnerabilities.isnull().sum()

mode = vulnerabilities.mode().values[0]

median = vulnerabilities.median()

q1 = vulnerabilities.quantile(0.25)
q3 = vulnerabilities.quantile(0.75)

max_value = vulnerabilities.max()
min_value = vulnerabilities.min()

print("Número de observaciones:", num_observations)
print("Número de valores ausentes:", num_missing_values)
print("Moda:", mode)
print("Mediana:", median)
print("Cuartil Q1:", q1)
print("Cuartil Q3:", q3)
print("Valor máximo:", max_value)
print("Valor mínimo:", min_value)

conn.close()
