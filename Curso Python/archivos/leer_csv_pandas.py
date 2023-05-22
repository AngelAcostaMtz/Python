import pandas as pd

#definiendo los dataframes
df = pd.read_csv("archivos\\csv.txt")
df2 = pd.read_csv("archivos\\csv.txt")


nombres = df["Nombre"]

ordena = df.sort_values("edad")

concatena = pd.concat([df,df2])

primer_fila = df.head(2)

ultimas_filas = df.tail(2)

filas_totales,columnas_totales = df.shape

apellidos = df.iloc[:,2]

print(apellidos)
