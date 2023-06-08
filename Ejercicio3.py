import sqlite3
import pandas as pd
import statistics
import numpy as np
import collections

con = sqlite3.connect('Database.db')

query = con.execute("SELECT * FROM alertas WHERE STRFTIME('%m',timestamp) = '07' AND PRIORITY = 1")
data_col = []
for column in query.description:
	data_col.append(column[0])
dAlertsJul1 = pd.DataFrame.from_records(data=query.fetchall(), columns=data_col)

query = con.execute("SELECT * FROM alertas WHERE STRFTIME('%m',timestamp ) = '07' AND PRIORITY = 2")
data_col = []
for column in query.description:
	data_col.append(column[0])
dAlertsJul2 = pd.DataFrame.from_records(data=query.fetchall(), columns=data_col)

query = con.execute("SELECT * FROM alertas WHERE STRFTIME('%m',timestamp ) = '07' AND PRIORITY = 3")
data_col = []
for column in query.description:
	data_col.append(column[0])
dAlertsJul3 = pd.DataFrame.from_records(data=query.fetchall(), columns=data_col)

query = con.execute("SELECT * FROM alertas WHERE STRFTIME('%m',timestamp ) = '08' AND PRIORITY = 1")
data_col = []
for column in query.description:
	data_col.append(column[0])
dAlertsAgo1 = pd.DataFrame.from_records(data=query.fetchall(), columns=data_col)

query = con.execute("SELECT * FROM alertas WHERE STRFTIME('%m',timestamp ) = '08' AND PRIORITY = 2")
data_col = []
for column in query.description:
	data_col.append(column[0])
dAlertsAgo2 = pd.DataFrame.from_records(data=query.fetchall(), columns=data_col)

query = con.execute("SELECT * FROM alertas WHERE STRFTIME('%m',timestamp ) = '08' AND PRIORITY = 3")
data_col = []
for column in query.description:
	data_col.append(column[0])
dAlertsAgo3 = pd.DataFrame.from_records(data=query.fetchall(), columns=data_col)

cursor = con.cursor()

#Número de observaciones y valores ausentes (mostrados como "Otras fechas" u "Otras alertas")
cursor.execute(''' 
    SELECT 
        CASE 
            WHEN priority = 1 THEN 'Alertas graves' 
            WHEN priority = 2 THEN 'Alertas medias' 
            WHEN priority = 3 THEN 'Alertas bajas' 
            ELSE 'Otras alertas' 
        END AS prioridad, 
        CASE 
            WHEN timestamp BETWEEN '2022-07-01 00:00:00' AND '2022-07-31 23:59:59' THEN 'Julio' 
            WHEN timestamp BETWEEN '2022-08-01 00:00:00' AND '2022-08-31 23:59:59' THEN 'Agosto' 
            ELSE 'Otras fechas' 
        END AS mes, 
        COUNT(*) AS cantidad 
    FROM alertas 
    GROUP BY prioridad, mes; 
''')

for row in cursor:
    print(row)

#Moda
print("\n")
conn = sqlite3.connect('Practica1.db')
cursor = conn.cursor()
cursor.execute("SELECT priority FROM alertas")
data = cursor.fetchall()
moda = statistics.mode(data)
conn.close()

print("La moda es", moda[0])

#Mediana
print("\n")
conn = sqlite3.connect('Practica1.db')
cursor = conn.cursor()
cursor.execute("SELECT priority FROM alertas")
data = cursor.fetchall()
mediana = statistics.median(data)
conn.close()

print("La mediana es", mediana[0])

#Cuartiles Q1 y Q3
print("\n")
conn = sqlite3.connect('Practica1.db')
cursor = conn.cursor()
cursor.execute("SELECT priority FROM alertas")
data = cursor.fetchall()
data_array = np.array(data)
q1 = np.percentile(data_array, 25)
q3 = np.percentile(data_array, 75)
conn.close()

print("El primer cuartil (Q1) es", q1)
print("El tercer cuartil (Q3) es", q3)

#Valores Máximos y mínimos
print("\n")
conn = sqlite3.connect('Practica1.db')
cursor = conn.cursor()

# Obtención del valor máximo y mínimo
conn = sqlite3.connect('Practica1.db')
cursor = conn.cursor()

# Consulta para obtener los valores máximos y mínimos por mes y prioridad
cursor.execute("""
    SELECT strftime('%Y-%m', timestamp) AS mes, priority, MAX(priority) AS max_value, MIN(priority) AS min_value
    FROM alertas
    GROUP BY mes, priority
""")
results = cursor.fetchall()

# Cálculo de los valores máximos y mínimos por prioridad y mes
conn = sqlite3.connect('Practica1.db')
cursor = conn.cursor()

# Consulta para obtener los valores mínimos y máximos por mes y prioridad
cursor.execute("""
    SELECT strftime('%Y-%m', timestamp) AS mes, priority, COUNT(*) AS cantidad
    FROM alertas
    WHERE mes IN ('2022-07', '2022-08')
    GROUP BY mes, priority
""")
results = cursor.fetchall()

valoresMax = collections.defaultdict(lambda: (0, ''))
valoresMin = collections.defaultdict(lambda: (float('inf'), ''))
for mes, priority, cantidad in results:
    if cantidad > valoresMax[priority][0]:
        valoresMax[priority] = (cantidad, mes)
    if cantidad < valoresMin[priority][0]:
        valoresMin[priority] = (cantidad, mes)

alertasTotales = collections.defaultdict(int)
for mes, priority, cantidad in results:
    alertasTotales[mes] += cantidad

mesMaxTotal = max(alertasTotales, key=alertasTotales.get)
mesMinTotal = min(alertasTotales, key=alertasTotales.get)
conn.close()
for priority in sorted(valoresMin):
    min_value, mesMin = valoresMin[priority]
    max_value, mesMax = valoresMax[priority]
    print(f"El valor mínimo de alertas de prioridad {priority} ha sido de {min_value}, en el mes de {mesMin}")
    print(f"El valor máximo de alertas de prioridad {priority} ha sido de {max_value}, en el mes de {mesMax}")
    print()

print(f"El mes con más alertas totales es {mesMaxTotal} con {alertasTotales[mesMaxTotal]} alertas")
print(f"El mes con menos alertas totales es {mesMinTotal} con {alertasTotales[mesMinTotal]} alertas")

con.close()