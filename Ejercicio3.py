import sqlite3
import pandas as pd

con = sqlite3.connect('Database.db')

# Cargar los datos de la base de datos en un DataFrame
df = pd.read_sql_query("SELECT * FROM alertas INNER JOIN dispositivos ON alertas.origin = dispositivos.ip OR alertas.destination = dispositivos.ip", con)

# Convertir el formato de la columna 'timestamp' a datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Filtrar por las alertas en julio y agosto
df_july_august = df[(df['timestamp'].dt.month == 7) | (df['timestamp'].dt.month == 8) | (df['timestamp'].dt.month == 9)]

# Agrupar por prioridad de alerta y fecha
grouped = df_july_august.groupby(['priority', df_july_august['timestamp'].dt.month])

# Calcular la información requerida para la variable de vulnerabilidades detectadas
vulnerabilities_info = grouped['analisis_vulnerabilidadesdetectadas'].agg(['count', lambda x: x.isnull().sum(), lambda x: x.mode().iloc[0], 'median', 'quantile', 'min', 'max'])

# Renombrar las columnas para mayor claridad
vulnerabilities_info.columns = ['Número de observaciones', 'Número de valores ausentes', 'Moda', 'Mediana', 'Cuartiles', 'Valor mínimo', 'Valor máximo']

print(vulnerabilities_info)


num_observaciones = df.shape[0]

num_valores_ausentes = df.isnull().sum().sum()
df_sept=df[df['timestamp'].dt.month == 9]
moda = df['analisis_vulnerabilidadesdetectadas'].mode().iloc[0]

mediana = df['analisis_vulnerabilidadesdetectadas'].median()

q1 = df['analisis_vulnerabilidadesdetectadas'].quantile(0.25)
q3 = df['analisis_vulnerabilidadesdetectadas'].quantile(0.75)

valor_minimo = df['analisis_vulnerabilidadesdetectadas'].min()
valor_maximo = df['analisis_vulnerabilidadesdetectadas'].max()

print("El número total de observaciones es", num_observaciones)
print("El número de valores nulos o ausentes es de", num_valores_ausentes+df_sept['timestamp'].count())
print("La moda es", vulnerabilities_info['Moda'])
print("La mediana es", vulnerabilities_info['Mediana'])
print("El cuartil 1 (Q1) es", q1)
print("El cuartil 3 (Q3) es", q3)
print("El valor mínimo es", valor_minimo)
print("El valor máximo es", valor_maximo)


con.close()