# EJERCICIO 3
#Para crear en una base de datos los datos del archivo alerts.csv

import sqlite3
import csv
import pandas as pd


#Para agrupar por prioridad de alerta y fecha
con = sqlite3.connect('Practica1.db')

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
if (dAlertsJul1["sid"].count() > dAlertsJul2["sid"].count()) & (dAlertsJul1["sid"].count() > dAlertsJul3["sid"].count()):
    modaJulio = 1
elif dAlertsJul2["sid"].count() > dAlertsJul3["sid"].count():
    modaJulio = 2
else:
    modaJulio = 3

if (dAlertsAgo1["sid"].count() > dAlertsAgo2["sid"].count()) & (dAlertsAgo1["sid"].count() > dAlertsAgo3["sid"].count()):
    modaAgosto = 1
elif dAlertsAgo2["sid"].count() > dAlertsAgo3["sid"].count():
    modaAgosto = 2
else:
    modaAgosto = 3

if ((dAlertsJul1["sid"].count()+dAlertsAgo1["sid"].count()) > (dAlertsJul2["sid"].count()+dAlertsAgo2["sid"].count())) & ((dAlertsJul1["sid"].count()+dAlertsAgo1["sid"].count()) > (dAlertsJul3["sid"].count()+dAlertsAgo3["sid"].count())):
    modaTot = 1
elif (dAlertsJul2["sid"].count()+dAlertsAgo2["sid"].count()) > (dAlertsJul3["sid"].count()+dAlertsAgo3["sid"].count()):
    modaTot = 2
else:
    modaTot = 3


print("La moda de la prioridad de las alertas en julio es", modaJulio)
print("La moda de la prioridad de las alertas en agosto es", modaAgosto)
print("La moda de la prioridad de todas las alertas es", modaTot)

#Mediana
print("\n")
Alertas1 = (dAlertsJul1["sid"].count()+dAlertsAgo1["sid"].count())
Alertas2 = (dAlertsJul2["sid"].count()+dAlertsAgo2["sid"].count())
Alertas3 = (dAlertsJul3["sid"].count()+dAlertsAgo3["sid"].count())
AlertasJulio = dAlertsJul1["sid"].count()+dAlertsJul2["sid"].count()+dAlertsJul3["sid"].count()
AlertasAgosto = dAlertsAgo1["sid"].count()+dAlertsAgo2["sid"].count()+dAlertsAgo3["sid"].count()
AlertasTot = Alertas1+Alertas2+Alertas3

if dAlertsJul1["sid"].count() >= ((AlertasJulio+1)/2):
    medianaJulio = 1
elif ((AlertasJulio+1)/2)-dAlertsJul1["sid"].count() == 0.5:
    medianaJulio = 1.5
elif dAlertsJul1["sid"].count()+dAlertsJul2["sid"].count() >= ((AlertasJulio+1)/2):
    medianaJulio = 2
elif ((AlertasJulio+1)/2)-(dAlertsJul1["sid"].count()+dAlertsJul2["sid"].count()) == 0.5:
    medianaJulio = 2.5
else:
    medianaJulio = 3

if dAlertsAgo1["sid"].count() >= ((AlertasAgosto+1)/2):
    medianaAgosto = 1
elif ((AlertasAgosto+1)/2)-dAlertsAgo1["sid"].count() == 0.5:
    medianaAgosto = 1.5
elif dAlertsAgo1["sid"].count()+dAlertsAgo2["sid"].count() >= ((AlertasAgosto+1)/2):
    medianaAgosto = 2
elif ((AlertasAgosto+1)/2)-(dAlertsAgo1["sid"].count()+dAlertsAgo2["sid"].count()) == 0.5:
    medianaAgosto = 2.5
else:
    medianaAgosto = 3

if Alertas1 >= ((AlertasTot+1)/2):
    medianaTot = 1
elif ((AlertasTot+1)/2)-Alertas1 == 0.5:
    medianaTot = 1.5
elif Alertas1+Alertas2 >= ((AlertasTot+1)/2):
    medianaTot = 2
elif ((AlertasTot+1)/2)-(Alertas1+Alertas2) == 0.5:
    medianaTot = 2.5
else:
    medianaTot = 3

print("La mediana de las alertas del mes de julio es la alerta de número", medianaJulio)
print("La mediana de las alertas del mes de agosto es la alerta de número", medianaAgosto)
print("La mediana de todas las alertas es la alerta número", medianaTot)


#Cuartiles Q1 y Q3
print("\n")
Alertas1 = (dAlertsJul1["sid"].count()+dAlertsAgo1["sid"].count())
Alertas2 = (dAlertsJul2["sid"].count()+dAlertsAgo2["sid"].count())
Alertas3 = (dAlertsJul3["sid"].count()+dAlertsAgo3["sid"].count())
AlertasJulio = dAlertsJul1["sid"].count()+dAlertsJul2["sid"].count()+dAlertsJul3["sid"].count()
AlertasAgosto = dAlertsAgo1["sid"].count()+dAlertsAgo2["sid"].count()+dAlertsAgo3["sid"].count()
AlertasTot = Alertas1+Alertas2+Alertas3

if dAlertsJul1["sid"].count() >= ((AlertasJulio+1)/4):
    Q1Julio = 1
elif ((AlertasJulio+1)/4)-dAlertsJul1["sid"].count() == 0.5:
    Q1Julio = 1.5
elif dAlertsJul1["sid"].count()+dAlertsJul2["sid"].count() >= ((AlertasJulio+1)/4):
    Q1Julio = 2
elif ((AlertasJulio+1)/4)-(dAlertsJul1["sid"].count()+dAlertsJul2["sid"].count()) == 0.5:
    Q1Julio = 2.5
else:
    Q1Julio = 3

if dAlertsAgo1["sid"].count() >= ((AlertasAgosto+1)/4):
    Q1Agosto = 1
elif ((AlertasAgosto+1)/4)-dAlertsAgo1["sid"].count() == 0.5:
    Q1Agosto = 1.5
elif dAlertsAgo1["sid"].count()+dAlertsAgo2["sid"].count() >= ((AlertasAgosto+1)/4):
    Q1Agosto = 2
elif ((AlertasAgosto+1)/4)-(dAlertsAgo1["sid"].count()+dAlertsAgo2["sid"].count()) == 0.5:
    Q1Agosto = 2.5
else:
    Q1Agosto = 3

if Alertas1 >= ((AlertasTot+1)/4):
    Q1Tot = 1
elif ((AlertasTot+1)/4)-Alertas1 == 0.5:
    Q1Tot = 1.5
elif Alertas1+Alertas2 >= ((AlertasTot+1)/4):
    Q1Tot = 2
elif ((AlertasTot+1)/4)-(Alertas1+Alertas2) == 0.5:
    Q1Tot = 2.5
else:
    Q1Tot = 3

print("El cuartil 1 (Q1) de las alertas del mes de julio es la alerta de número", Q1Julio)
print("El cuartil 1 (Q1) de las alertas del mes de agosto es la alerta de número", Q1Agosto)
print("El cuartil 1 (Q1) de todas las alertas es la alerta número", Q1Tot)

if dAlertsJul1["sid"].count() >= (((AlertasJulio+1)*3)/4):
    Q3Julio = 1
elif (((AlertasJulio+1)*3)/4)-dAlertsJul1["sid"].count() == 0.5:
    Q3Julio = 1.5
elif dAlertsJul1["sid"].count()+dAlertsJul2["sid"].count() >= (((AlertasJulio+1)*3)/4):
    Q3Julio = 2
elif (((AlertasJulio+1)*3)/4)-(dAlertsJul1["sid"].count()+dAlertsJul2["sid"].count()) == 0.5:
    Q3Julio = 2.5
else:
    Q3Julio = 3

if dAlertsAgo1["sid"].count() >= (((AlertasAgosto+1)*3)/4):
    Q3Agosto = 1
elif (((AlertasAgosto+1)*3)/4)-dAlertsAgo1["sid"].count() == 0.5:
    Q3Agosto = 1.5
elif dAlertsAgo1["sid"].count()+dAlertsAgo2["sid"].count() >= (((AlertasAgosto+1)*3)/4):
    Q3Agosto = 2
elif (((AlertasAgosto+1)*3)/4)-(dAlertsAgo1["sid"].count()+dAlertsAgo2["sid"].count()) == 0.5:
    Q3Agosto = 2.5
else:
    Q3Agosto = 3

if Alertas1 >= (((AlertasTot+1)*3)/4):
    Q3Tot = 1
elif ((AlertasTot+1)*3)/4-Alertas1 == 0.5:
    Q3Tot = 1.5
elif Alertas1+Alertas2 >= ((AlertasTot+1)*3)/4:
    Q3Tot = 2
elif (((AlertasTot+1)*3)/4)-(Alertas1+Alertas2) == 0.5:
    Q3Tot = 2.5
else:
    Q3Tot = 3

print("El cuartil 3 (Q3) de las alertas del mes de julio es la alerta de número", Q3Julio)
print("El cuartil 3 (Q3) de las alertas del mes de agosto es la alerta de número", Q3Agosto)
print("El cuartil 3 (Q3) de todas las alertas es la alerta número", Q3Tot)

#Valores Máximos y mínimos
print("\n")
valorMinJulio = 0
valorMaxJulio = 0
valorMinAgosto = 0
valorMaxAgosto = 0

if dAlertsJul1["sid"].count() < (dAlertsJul2["sid"].count()) & (dAlertsJul1["sid"].count() < (dAlertsJul3["sid"].count())):
    valorMinJulio = dAlertsJul1["sid"].count()
elif dAlertsJul2["sid"].count() < dAlertsJul3["sid"].count():
    valorMinJulio = dAlertsJul2["sid"].count()
else:
    valorMinJulio = dAlertsJul3["sid"].count()

if dAlertsJul1["sid"].count() > (dAlertsJul2["sid"].count()) & (dAlertsJul1["sid"].count() > (dAlertsJul3["sid"].count())):
    valorMaxJulio = dAlertsJul1["sid"].count()
elif dAlertsJul2["sid"].count() > dAlertsJul3["sid"].count():
    valorMaxJulio = dAlertsJul2["sid"].count()
else:
    valorMaxJulio = dAlertsJul3["sid"].count()

if dAlertsAgo1["sid"].count() < (dAlertsAgo2["sid"].count()) & (dAlertsAgo1["sid"].count() < (dAlertsAgo3["sid"].count())):
    valorMinAgosto = dAlertsAgo1["sid"].count()
elif dAlertsAgo2["sid"].count() < dAlertsAgo3["sid"].count():
    valorMinAgosto = dAlertsAgo2["sid"].count()
else:
    valorMinAgosto = dAlertsAgo3["sid"].count()

if dAlertsAgo1["sid"].count() > (dAlertsAgo2["sid"].count()) & (dAlertsAgo1["sid"].count() > (dAlertsAgo3["sid"].count())):
    valorMaxAgosto = dAlertsAgo1["sid"].count()
elif dAlertsAgo2["sid"].count() > dAlertsAgo3["sid"].count():
    valorMaxAgosto = dAlertsAgo2["sid"].count()
else:
    valorMaxAgosto = dAlertsAgo3["sid"].count()

valorMin1 = 0
valorMax1 = 0
valorMin2 = 0
valorMax2 = 0
valorMin3 = 0
valorMax3 = 0

mesMin1 = ""
mesMax1 = ""
mesMin2 = ""
mesMax2 = ""
mesMin3 = ""
mesMax3 = ""

if dAlertsJul1["sid"].count() < dAlertsAgo1["sid"].count():
    valorMin1 = dAlertsJul1["sid"].count()
    valorMax1 = dAlertsAgo1["sid"].count()
    mesMin1 = "julio"
    mesMax1 = "agosto"
else:
    valorMin1 = dAlertsAgo1["sid"].count()
    valorMax1 = dAlertsJul1["sid"].count()
    mesMin1 = "agosto"
    mesMax1 = "julio"

if dAlertsJul2["sid"].count() < dAlertsAgo2["sid"].count():
    valorMin2 = dAlertsJul2["sid"].count()
    valorMax2 = dAlertsAgo2["sid"].count()
    mesMin2 = "julio"
    mesMax2 = "agosto"
else:
    valorMin2 = dAlertsAgo2["sid"].count()
    valorMax2 = dAlertsJul2["sid"].count()
    mesMin2 = "agosto"
    mesMax2 = "julio"

if dAlertsJul3["sid"].count() < dAlertsAgo3["sid"].count():
    valorMin3 = dAlertsJul3["sid"].count()
    valorMax3 = dAlertsAgo3["sid"].count()
    mesMin3 = "julio"
    mesMax3 = "agosto"
else:
    valorMin3 = dAlertsAgo3["sid"].count()
    valorMax3 = dAlertsJul3["sid"].count()
    mesMin3 = "agosto"
    mesMax3 = "julio"

valorMinTotal = 0
valorMaxTotal = 0

mesMinTotal = ""
mesMaxTotal = ""

if dAlertsJul1["sid"].count()+dAlertsJul2["sid"].count()+dAlertsJul3["sid"].count() < dAlertsAgo1["sid"].count()+dAlertsAgo2["sid"].count()+dAlertsAgo3["sid"].count():
    valorMinTotal = dAlertsJul1["sid"].count()+dAlertsJul2["sid"].count()+dAlertsJul3["sid"].count()
    valorMaxTotal = dAlertsAgo1["sid"].count() + dAlertsAgo2["sid"].count() + dAlertsAgo3["sid"].count()
    mesMinTotal = "julio"
    mesMaxTotal = "agosto"
else:
    valorMaxTotal = dAlertsJul1["sid"].count() + dAlertsJul2["sid"].count() + dAlertsJul3["sid"].count()
    valorMinTotal = dAlertsAgo1["sid"].count() + dAlertsAgo2["sid"].count() + dAlertsAgo3["sid"].count()
    mesMinTotal = "agosto"
    mesMaxTotal = "julio"

print("El valor mínimo de alertas de prioridad 1 ha sido de", valorMin1, ", en el mes de", mesMin1)
print("El valor máximo de alertas de prioridad 1 ha sido de", valorMax1, ", en el mes de", mesMax1)
print("El valor mínimo de alertas de prioridad 2 ha sido de", valorMin2, ", en el mes de", mesMin2)
print("El valor máximo de alertas de prioridad 2 ha sido de", valorMax2, ", en el mes de", mesMax2)
print("El valor mínimo de alertas de prioridad 3 ha sido de", valorMin3, ", en el mes de", mesMin3)
print("El valor máximo de alertas de prioridad 3 ha sido de", valorMax3, ", en el mes de", mesMax3)

print("El valor mínimo de alertas totales ha sido de", valorMinTotal, ", en el mes de", mesMinTotal)
print("El valor máximo de alertas totales ha sido de", valorMaxTotal, ", en el mes de", mesMaxTotal)


con.close()