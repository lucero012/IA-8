from datetime import datetime

nom=input("Ingresa tu  nombre: ")
pro=input("Ingresa el nombre del producto: ")
ti=input("Ingresa el nombre de la tienda: ")
fo=input("Ingresa el folio : ")
total_compra= float(input("Ingresa el total de tu compra: "))

fyh= datetime.now()
if total_compra > 100:
    descuento= total_compra * 0.10
    total_final= total_compra - descuento
    print(f" \n\n============ TICKET DE COMPRA ============ \n"
          f"Tienda: {ti} \n"
          f"Folio: {fo} \n"
          f"Fecha y Hora: {fyh}\n"
          f" ---------------------------------------------\n"
          f"Cliente: {nom}\n"
          f"Producto: {pro}\n"
          f"Total de la compra: $ {total_compra}\n"
          f"Descuento aplicado: $ {descuento}\n"
          f"Total a pagar= $ {total_final}\n"
          f"--------------------------------------------\n"
         f" ¡Gracias por tu compra! -- {nom} -- ¡Vuelve Pronto!\n\n")

          
else:
    print(f" \n\n============ TICKET DE COMPRA ============ \n"
          f"Tienda: {ti} \n"
          f"Folio: {fo} \n"
          f"Fecha y Hora: {fyh}\n"
          f" ---------------------------------------------\n"
          f"Cliente: {nom}\n"
          f"Producto: {pro}\n"
          f"Total de la compra: $ {total_compra}\n"
          f"--------------------------------------------\n"
         f" ¡Gracias por tu compra! -- {nom} -- ¡Vuelve Pronto!\n\n")
    
