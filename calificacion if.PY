calif = int(input("Introduce la calificación: "))
mat= input("Introduce el nombre de la materia: ")


if 95 <= calif <= 100:
    print(f"La calificación {calif} es Excelente")
elif 85 <= calif < 95:
    print(f"La calificación {calif} es Buena")
elif 75 <= calif < 85:
    print(f"La calificación {calif} es Regular")
elif 70 <= calif < 75:
    print(f"La calificación {calif} es Suficiente")
else:
    print(f"La calificación {calif} es Insuficiente")

print (f"el nombre de la materia es: {mat}")