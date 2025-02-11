nom=input("Ingresa tu  nombre: ")
pro=input("Ingresa el nombre del producto: ")

total_compra= float(input("Ingresa el total de tu compra: "))
if total_compra > 100:
    descuento= total_compra * 0.10
    total_final= total_compra - descuento
    print(f"¡Felicidades {nom}! Tienes un descuento del 10% de tu procucto {pro}  \n El total a pagar es: {total_final}")
else:
    print(f"El total a pagar es: {total_compra}")
    
