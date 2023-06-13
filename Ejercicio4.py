import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('Database.db')

df_alertas = pd.read_sql_query("SELECT * FROM alertas", conn)
df_dispositivos = pd.read_sql_query("SELECT * FROM dispositivos", conn)

conn.close()

# 10 IP de origen más problemáticas
fig1, ax1 = plt.subplots(figsize=(7, 12))
ip_problematicas = df_alertas[df_alertas['priority'] == 1]['origin'].value_counts().nlargest(10)
ip_problematicas.plot(kind='bar', ax=ax1)
plt.title('Top 10 IP de origen más problemáticas')
plt.xlabel('IP de origen')
plt.ylabel('Número de alertas')
plt.show()

# Número de alertas en el tiempo
fig2, ax2 = plt.subplots(figsize=(10, 10))
df_alertas['timestamp'] = pd.to_datetime(df_alertas['timestamp'])
df_alertas['fecha'] = df_alertas['timestamp'].dt.date
df_alertas['fecha'].value_counts().sort_index().plot(kind='bar', ax=ax2)
plt.title('Número de alertas en el tiempo')
plt.xlabel('Fecha')
plt.ylabel('Número de alertas')
plt.xticks(rotation=90)
plt.show()

# Porcentaje del total del número de alertas por categoría )
fig3, ax3 = plt.subplots(figsize=(15, 15))
porcentaje_categorias = df_alertas['clasification'].value_counts(normalize=True) * 100
porcentaje_categorias.plot(kind='pie', autopct='%1.1f%%', ax=ax3)
plt.title('Porcentaje de alertas por categoría')
plt.ylabel('')
plt.axis('equal')
plt.show()

# Dispositivos más vulnerables
fig4, ax4 = plt.subplots(figsize=(8, 10))
df_dispositivos['vulnerabilidades_totales'] = df_dispositivos['analisis_serviciosinseguros'] + df_dispositivos['analisis_vulnerabilidadesdetectadas']
dispositivos_vulnerables = df_dispositivos[['ip', 'vulnerabilidades_totales']].sort_values(by='vulnerabilidades_totales', ascending=False).head(10)
dispositivos_vulnerables.plot(x='ip', y='vulnerabilidades_totales', kind='bar', ax=ax4)
plt.title('Dispositivos más vulnerables')
plt.xlabel('IP del dispositivo')
plt.ylabel('Suma de servicios vulnerables y vulnerabilidades detectadas')
plt.show()

# Media de puertos abiertos frente a servicios inseguros y frente al total de servicios detectados
fig5, ax5 = plt.subplots(figsize=(8, 6))
df_dispositivos['media_puertos_abiertos'] = df_dispositivos['analisis_puertosabiertos'].apply(lambda x: len(eval(x)) if x != 'None' else 0)
media_puertos_abiertos = df_dispositivos['media_puertos_abiertos'].mean()
media_servicios_inseguros = df_dispositivos['analisis_serviciosinseguros'].mean()
media_total_servicios = df_dispositivos['analisis_servicios'].mean()
datos = [media_puertos_abiertos, media_servicios_inseguros, media_total_servicios]
etiquetas = ['Media de puertos abiertos', 'Media de servicios inseguros', 'Media del total de servicios']
ax5.bar(etiquetas, datos)
plt.title('Comparación de medias')
plt.ylabel('Cantidad')
plt.show()