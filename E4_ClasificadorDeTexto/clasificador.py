import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn import metrics


textos = [
    "Me encanta esta casa, es espaciosa y luminosa",
    "No me gustó la casa, está en mal estado",
    "Excelente ubicación y diseño moderno",
    "Terrible, la casa es muy pequeña y oscura",
    "Muy recomendable, una casa cómoda y bien ubicada",
    "Horrible, no recomendaría esta casa a nadie",
]

etiquetas = [1, 0, 1, 0, 1, 0]  


X_train, X_test, y_train, y_test = train_test_split(textos, etiquetas, test_size=0.2, random_state=42)


modelo = make_pipeline(TfidfVectorizer(), MultinomialNB())
modelo.fit(X_train, y_train)

predicciones = modelo.predict(textos)


print("\nClasificación de opiniones sobre casas: \n")
for texto, prediccion in zip(textos, predicciones):
    resultado = "Positiva" if prediccion == 1 else "Negativa"
    print(f"Opinión: \"{texto}\" → Clasificación: {resultado}")


predicciones_test = modelo.predict(X_test)
print("\nPrecisión en datos de prueba:", metrics.accuracy_score(y_test, predicciones_test))
print("Reporte de clasificación:\n", metrics.classification_report(y_test, predicciones_test, zero_division=0))
