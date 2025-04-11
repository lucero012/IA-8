import nltk
from nltk.sem.logic import Expression
 
 #Inicializar el analizador
read_expr = Expression.fromstring

# Definir las constantes 
mary = read_expr('mary')
lucero = read_expr('lucero')
maria = read_expr('maria')

#Definir los predicados con las constantes
amigos_mary_lucero = read_expr('amigos(mary, lucero)')
amigos_mary_maria = read_expr('no_son_amigos(mary, maria)')
no_amigos_maria_lucero = read_expr('tienen_la_misma_edad(maria, lucero)')
trabajan_juntos_mary_lucero = read_expr('trabajan(mary, lucero)')

#Crear un conjunto de fórmulas
formulas = [
    amigos_mary_lucero,
    amigos_mary_maria,
    no_amigos_maria_lucero,
    trabajan_juntos_mary_lucero
]
 # Imprimir las fórmulas
for formula in formulas:
    print(f"{formula} : {formula}")