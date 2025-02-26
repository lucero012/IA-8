import os

def menu():
    while True:
        print("\nMenú:")
        print("1. Adivinar número")
        print("2. Algoritmo")
        print("3. AreaCir")
        print("4. Calificación if")
        print("5. CicloFor")
        print("6. CondicionIf")
        print("7. DeclaracionVariables")
        print("8. DemostracionTeoremas")
        print("9. Descuento")
        print("10. Empirismo2")
        print("11. Exploracion")
        print("12. Grafo")
        print("13. Heuristica")
        print("14. Informacion")
        print("15. MateriaCalif")
        print("16. MayorQue")
        print("17. MostrarCalifXletra")
        print("18. Multiagente")
        print("19. Nodo")
        print("20. ParImpar")
        print("21. PositivoNegativo")
        print("22. Resta-Multiplicacion")
        print("23. Suma")
        print("24. TemperaturaCiudad")
        print("25. TemperaturaCiudad2")
        print("26. Ticket")
        print("27. TomaDecisiones")
        print("28. UsoDatetime")
        print("29. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        archivos = [
            "AdivinarNumero.py", "Algoritmo.py", "AreaCir.py", "calificacion_if.py", "CicloFor.py",
            "CondicionIf.py", "DeclaracionVariables.py", "DemostracionTeoremas.py", "Descuento.py",
            "Empirismo2.py", "Exploracion.py", "grafo.py", "Heuristica.py", "Informacion.py",
            "materiaCalif.py", "MayorQue.py", "MostrarCalifXletra.py", "Multiagente.py", "Nodo.py",
            "parImpar.py", "PositivoNegativo.py", "resta-multiplicacion.py", "Suma.py",
            "temperaturaCiudad.py", "TemperaturaCiudad2.py", "ticket.py", "TomaDecisiones.py", "UsoDatetime.py"
        ]
        
        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 28:
                os.system(f"python {archivos[opcion - 1]}")
                input("\nPresione Enter para continuar...")
            elif opcion == 29:
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intente de nuevo.")
        else:
            print("Ingrese un número válido.")

if __name__ == "__main__":
    menu()
