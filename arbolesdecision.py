import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

# Solicitar la fuente de datos al usuario
fuente_datos = input("Ingrese la ruta del archivo CSV o URL con los datos: ").strip()

# Cargar los datos
try:
    datos = pd.read_csv(fuente_datos)
    print("Datos cargados exitosamente.")
except Exception as e:
    print(f"Error al cargar los datos: {e}")
    exit()

# Mostrar las primeras filas de los datos
print("\nPrimeras filas de los datos:")
print(datos.head())

# Preprocesamiento de los datos
# Manejar datos faltantes
imputador = SimpleImputer(strategy="mean")  # Reemplazar valores faltantes numéricos con la media
datos.iloc[:, :] = imputador.fit_transform(datos)

# Codificar variables categóricas si es necesario
for columna in datos.select_dtypes(include=["object"]).columns:
    le = LabelEncoder()
    datos[columna] = le.fit_transform(datos[columna])

# Separar características (X) y etiquetas (y)
X = datos.iloc[:, :-1]  # Todas las columnas excepto la última
y = datos.iloc[:, -1]   # Última columna (aprobado/rechazado)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar el modelo de Random Forest
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Evaluar el modelo
y_pred = modelo.predict(X_test)
print("\nEvaluación del modelo:")
print(f"Precisión: {accuracy_score(y_test, y_pred):.2f}")
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred))

# Permitir ingresar nuevos datos manualmente para predicción
print("\nIngrese los datos del cliente para predecir si se aprueba o no el crédito:")
nuevos_datos = []
for columna in X.columns:
    valor = float(input(f"Ingrese el valor para {columna}: "))
    nuevos_datos.append(valor)

# Convertir los datos ingresados a un formato adecuado para el modelo
nuevos_datos = np.array(nuevos_datos).reshape(1, -1)

# Realizar la predicción
prediccion = modelo.predict(nuevos_datos)
resultado = "Aprobado" if prediccion[0] == 1 else "Rechazado"
print(f"\nResultado de la predicción: {resultado}")