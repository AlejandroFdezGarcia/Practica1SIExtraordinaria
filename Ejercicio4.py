###################################### Para seleccionar las IP de origen más problemáticas y representarlas:
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

con = sqlite3.connect('Practica1.db')
cur = con.cursor()
cur.execute("SELECT origin, COUNT(*) FROM alertas WHERE priority = 1 GROUP BY origin ORDER BY COUNT(*) DESC LIMIT 10")

results = cur.fetchall()
con.close()

ips = [result[0] for result in results]
counts = [result[1] for result in results]

plt.bar(ips, counts)
plt.xlabel('IPs de origen')
plt.ylabel('Número de incidencias')
plt.title('Top 10 IPs de origen con mayor número de incidencias (prioridad = 1)')

plt.show()

############################### Número de alertas en el tiempo:
conn = sqlite3.connect('Practica1.db')
query = "SELECT timestamp FROM alertas"
df = pd.read_sql_query(query, conn)

df['timestamp'] = pd.to_datetime(df['timestamp'])

df['count'] = 1

alerts_per_day = df.groupby(df['timestamp'].dt.date)['count'].sum()

alerts_per_day.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Fecha')
plt.ylabel('Número de alertas')
plt.title('Número de alertas en el tiempo (por día)')
plt.show()

conn.close()