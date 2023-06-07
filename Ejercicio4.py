###################################### Para seleccionar las IP de origen más problemáticas y representarlas:
import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

con = sqlite3.connect('Practica1.db')
query = "SELECT origin, COUNT(*) as count FROM alertas WHERE priority = 1 GROUP BY origin ORDER BY count DESC LIMIT 10"
df = pd.read_sql_query(query, con)

con.close()

ips = df['origin']
counts = df['count']

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
query = "SELECT origin, COUNT(*) as total FROM alertas GROUP BY origin ORDER BY total DESC"
df = pd.read_sql_query(query, conn)

conn.close()

num_devices = 10
x_labels = df['origin'].head(num_devices)
y_values = df['total'].head(num_devices)

plt.figure(figsize=(15, 6))
plt.bar(x_labels, y_values)
plt.title(f"Top {num_devices} dispositivos más vulnerables")
plt.xlabel("Dispositivo")
plt.ylabel("Número de alertas")
plt.show()

##################################### Media de puertos abiertos:
conn = sqlite3.connect('Practica1.db')
query = "SELECT clasification, AVG(port) as avg_port, COUNT(*) as count FROM alertas GROUP BY clasification"
df = pd.read_sql_query(query, conn)

clasifications = df['clasification']
avg_ports = df['avg_port']
total_services = df['count']
insecure_services = pd.Series([0] * len(df))

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

conn.close()