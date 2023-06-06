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

plt.figure(figsize=(15, 6))
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

alerts_per_day.plot(kind='bar', figsize=(10, 12))
plt.xlabel('Fecha')
plt.ylabel('Número de alertas')
plt.title('Número de alertas en el tiempo (por día)')
plt.show()

conn.close()

############################# Porcentaje del total del número de alertas por categoría
conn = sqlite3.connect('Practica1.db')
query = "SELECT clasification, COUNT(*) as total FROM alertas GROUP BY clasification"
df = pd.read_sql_query(query, conn)

df['percentage'] = df['total'] / df['total'].sum() * 100

plt.figure(figsize=(15, 15))
plt.pie(df['percentage'], labels=df['clasification'], autopct='%1.1f%%')
plt.title('Porcentaje del total de alertas por categoría')
plt.axis('equal')
plt.show()

conn.close()

######################## Dispositivos más vulnerables:
conn = sqlite3.connect('Practica1.db')
cursor = conn.cursor()

query = "SELECT origin, COUNT(*) as total FROM alertas GROUP BY origin ORDER BY total DESC"

cursor.execute(query)
results = cursor.fetchall()

conn.close()

num_devices = 10
x_labels = [result[0] for result in results[:num_devices]]
y_values = [result[1] for result in results[:num_devices]]

plt.figure(figsize=(15, 6))
plt.bar(x_labels, y_values)
plt.title(f"Top {num_devices} dispositivos más vulnerables")
plt.xlabel("Dispositivo")
plt.ylabel("Número de alertas")
plt.show()



##################################### Media de puertos abiertos:
conn = sqlite3.connect('Practica1.db')

query = "SELECT clasification, AVG(port) as avg_port, COUNT(*) as count FROM alertas GROUP BY clasification"

cursor = conn.cursor()
cursor.execute(query)
results = cursor.fetchall()

clasifications = []
avg_ports = []
total_services = []
insecure_services = []

for row in results:
    clasification, avg_port, count = row
    clasifications.append(clasification)
    avg_ports.append(avg_port)
    total_services.append(count)
    insecure_services.append(0)

fig, ax = plt.subplots(figsize=(8, 22))
ax.bar(clasifications, avg_ports, label='Media de puertos abiertos')
ax.plot(clasifications, total_services, label='Total de servicios detectados', color='red')
ax.plot(clasifications, insecure_services, label='Servicios inseguros', color='orange')
ax.legend()
ax.set_xlabel('Clasificación')
ax.set_ylabel('Puertos')
ax.set_title('Media de puertos abiertos por clasificación de vulnerabilidad')
plt.xticks(rotation=90)
plt.show()