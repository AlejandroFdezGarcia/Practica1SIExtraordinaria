import pandas as pd
import sqlite3
import re

con = sqlite3.connect('Database.db')

df_dispositivos = pd.read_sql_query("SELECT * FROM dispositivos", con)
df_alertas = pd.read_sql_query("SELECT * FROM alertas", con)

num_dispositivos = len(df_dispositivos)
campos_missing = df_dispositivos.isnull().sum().sum()

num_alertas = len(df_alertas)

def extract_ports(port_string):
    if port_string == "None":
        return 0
    ports = re.findall(r'\d+', port_string)
    return len(ports)

df_dispositivos['analisis_puertosabiertos_num'] = df_dispositivos['analisis_puertosabiertos'].apply(extract_ports)

mediana_puertos_abiertos = df_dispositivos['analisis_puertosabiertos_num'].median()
moda_puertos_abiertos = df_dispositivos['analisis_puertosabiertos_num'].mode().values

mediana_serv_inseguros = df_dispositivos['analisis_serviciosinseguros'].median()
moda_serv_inseguros = df_dispositivos['analisis_serviciosinseguros'].mode().values

mediana_vuln_detectadas = df_dispositivos['analisis_vulnerabilidadesdetectadas'].median()
moda_vuln_detectadas = df_dispositivos['analisis_vulnerabilidadesdetectadas'].mode().values

min_puertos_abiertos = df_dispositivos['analisis_puertosabiertos_num'].min()
max_puertos_abiertos = df_dispositivos['analisis_puertosabiertos_num'].max()

min_vuln_detectadas = df_dispositivos['analisis_vulnerabilidadesdetectadas'].min()
max_vuln_detectadas = df_dispositivos['analisis_vulnerabilidadesdetectadas'].max()

print("Número de dispositivos:", num_dispositivos)
print("Campos missing o None:", campos_missing)
print("Número de alertas:", num_alertas)
print("Mediana de puertos abiertos:", mediana_puertos_abiertos)
print("Moda de puertos abiertos:", moda_puertos_abiertos)
print("Mediana de servicios inseguros detectados:", mediana_serv_inseguros)
print("Moda de servicios inseguros detectados:", moda_serv_inseguros)
print("Mediana de vulnerabilidades detectadas:", mediana_vuln_detectadas)
print("Moda de vulnerabilidades detectadas:", moda_vuln_detectadas)
print("Valor mínimo de puertos abiertos:", min_puertos_abiertos)
print("Valor máximo de puertos abiertos:", max_puertos_abiertos)
print("Valor mínimo de vulnerabilidades detectadas:", min_vuln_detectadas)
print("Valor máximo de vulnerabilidades detectadas:", max_vuln_detectadas)

con.close()
