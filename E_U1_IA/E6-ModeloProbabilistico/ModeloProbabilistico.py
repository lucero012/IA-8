from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Datos simulados: edad, ingresos (en miles) y si compró (1 = sí, 0 = no)
# Estos datos representan variables de entrada (predictoras) y una salida binaria (objetivo).
edad = [18, 25, 35, 45, 22, 28, 40, 50, 30, 60]
ingresos = [15, 20, 35, 50, 18, 25, 45, 55, 30, 60]
compra = [0, 0, 1, 1, 0, 0, 1, 1, 1, 1]

# Combinar edad e ingresos como características
X = [[e, i] for e, i in zip(edad, ingresos)]  # Variables predictoras
y = compra  # Variable objetivo

# Dividir datos en conjuntos de entrenamiento y prueba
# Esto permite evaluar el rendimiento del modelo en datos no vistos previamente.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear y entrenar el modelo probabilístico Naive Bayes Gaussiano
# Este modelo asume que las características siguen una distribución normal.
modelo = GaussianNB()
modelo.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
y_pred = modelo.predict(X_test)

# Evaluar el modelo usando precisión como métrica de rendimiento
precision = accuracy_score(y_test, y_pred)
print("Precisión del modelo probabilístico:", precision)

# Mostrar resultados detallados de las predicciones
print("\nResultados de predicción:")
for (e, i), real, pred in zip(X_test, y_test, y_pred):
    resultado = "Correcto" if real == pred else "Incorrecto"
    print(f"Edad: {e}, Ingresos: {i}k => Compra real: {'Sí' if real == 1 else 'No'}, "
          f"Predicción: {'Sí' if pred == 1 else 'No'} ({resultado})")

# Comentario sobre la utilidad del modelo
print("\nEl modelo probabilístico Naive Bayes utilizado aquí es ideal para problemas de clasificación en los que "
      "existen múltiples características predictoras, como la edad y los ingresos. Además, su enfoque probabilístico "
      "permite gestionar la incertidumbre en las predicciones, proporcionando una base sólida para investigaciones "
      "en inteligencia artificial relacionadas con el comportamiento del consumidor.")
