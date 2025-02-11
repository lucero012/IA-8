calif = int(input("Introduce la calificación: "))


if 90 <= calif <= 100:
    print(f"La calificación es: A")
elif 80 <= calif < 90:
    print(f"La calificación es: B")
elif 70 <= calif < 80:
    print(f"La calificación es: C")
elif 60 <= calif < 70:
    print(f"La calificación es. D")
else:
    print(f"La calificación es: E")