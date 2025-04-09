import numpy as np  # libreria para manejo de arreglos o matrices
import pandas as pd  # libreria para manejo de datos
#ahora vamos a trabajar con un archivo csv
df = pd.read_csv('archivo_dataset_python.csv')  # leer un archivo csv
print(df)  # imprimir el dataframe leido del csv

# ahora con las funciones de try
try:
    df2 = pd.read_csv('archivo_dataset_python.csv')  # leer un archivo csv
    print("El contenido del archivo es:")
    print(df2)  # imprimir el dataframe leido del csv
except FileNotFoundError:
    print("El archivo no se encontró.")     
except pd.errors.EmptyDataError:
    print("El archivo está vacío.")
