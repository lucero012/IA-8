from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Datos de entrenamiento ampliados
textos = [
    "Me encanta", "Odio esto", "Es excelente", "Es terrible", "Muy bueno", "Muy malo",
    "Hoy es un día muy bonito", "Estoy feliz", "Estoy triste", "Es un día perfecto",
    "No me gusta", "Es maravilloso", "Me siento mal", "Este lugar es genial", "Es horrible", "la vida es hermosa", "la vida es fea"
]
etiquetas = [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0,1,0]

# Modelo
X_train, X_test, y_train, y_test = train_test_split(textos, etiquetas, test_size=0.2, random_state=42)
vectorizador = TfidfVectorizer().fit(X_train)
modelo = MultinomialNB().fit(vectorizador.transform(X_train), y_train)

# Clasificación interactiva
opinion = input("Ingresa tu opinión: ")
opinion_vectorizada = vectorizador.transform([opinion])
prediccion = modelo.predict(opinion_vectorizada)[0]

print("Positiva (1)" if prediccion == 1 else "Negativa (0)")
