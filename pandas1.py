import numpy as np  # libreria para manejo de arreglos o matrices
import pandas as pd  # libreria para manejo de datos

# Imprimir la versión de la librería pandas
print(pd.__version__)  

a = [1, 2, 3, 4, 5]  # lista de numeros
myvar1 = pd.Series(a)  # convertir la lista en un objeto de la libreria pandas
print(myvar1)  # imprimir el objeto  

mydataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)  # Cambiar 'pandas' a 'pd'
print(myvar)

print(myvar.loc[0])  # Acceder a la primera fila del DataFrame
print(myvar.iloc[0])  # Acceder a la primera fila del DataFrame usando iloc

# dataframe indexado por nombre (dias):
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 

#ahora vamos a trabajar con un archivo csv
df = pd.read_csv('archivo_dataset_python.csv')  # leer un archivo csv
print(df)  # imprimir el dataframe leido del csv
#construir un json
