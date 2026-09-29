#Datos
# nombre_cliente = "      Juan Perez      "
# producto = "Dibujo"
# monto = 30000
# metodo_pago = "efectivo"
# telefono = "1234567899"
# cupon = "PROMO10"

#Programa
# nombre_formateado = nombre_cliente.strip().title()
# #print(nombre_formateado)

# #Telefono
# telefono_valido = telefono.isdigit()

# if telefono_valido:
#     print("numero de telefono valido")
# else:
#     print("numero de telefono invalido")

# #Como empieza el cupon (Validar)

# cupon_valido = cupon.startswith("PROMO") and cupon[-1].isdigit()
# termina_en_letra = cupon.endswith(("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"))

# #Calculo del envio del producto (montos)

# if monto < 10000:
#     envio = 1500
# elif monto < 30000:
#     envio = 800
# else:
#     envio = 0    

# # Calculo de descuento por metodo de pago

# match metodo_pago:
#     case "efectivo":
#         descuento = 0.10
#     case "transferencia":
#         descuento = 0.05
#     case "tarjeta":
#         descuento = 0.0
#     case _:
#         descuento = None

# if descuento == None:
#     print("X Metodo de pago invalido. No se puede procesar el pedido.")
# elif not telefono_valido:
#     print(f"X Telefono invalido. {telefono} debe contener numeros")
# else:

#     if cupon_valido:
#         descuento_total = descuento + 0.5
#     else:
#         descuento_total = descuento

#     monto_con_descuento = monto - (monto * descuento_total)
#     total_final = monto_con_descuento + envio

#     print(f"Cliente: {nombre_formateado}, producto: {producto}, telefono: {telefono}, cupon: {cupon}, monto original: {monto}, descuento total: {descuento_total}, envio: {envio} {'-'*10} Total final: {total_final}")

#______________________________________________________________________________________________________________________
# PREENTREGA
productos = []
opcion = ""

while opcion != "5":

    print("1. Agregar productos")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Elige una opcion (1-5): ").strip()

    if opcion == "1":
        print("Agregar producto")

        nombre = input("Ingresa el nombre del producto: ").strip()
        while nombre == "":
            print("El nombre no puede estar vacio")
            nombre = input("Ingresa el nombre del producto: ").strip()


        categoria = input("Ingresa la categoria de tu producto: ").strip()
        while nombre == "":
            print("La categoria no puede estar vacio")
            categoria = input("Ingresa la categoria de tu producto: ").strip()

        precio = input("Ingresa el precio de tu producto, sin centavos").strip()

        while not precio.isdigit() or int(precio) == 0:
            print("Elprecio debe ser un numero entero mayor a 0")
            precio = input("ingresa el precio de tu producto sin centavos").strip()

        #precio = int(precio)
        #productos = productos + [[nombre, categoria, precio]]

        productos.append([nombre, categoria, int(precio)])

    elif opcion == "2":
        print("Listar productos")
        if len(productos) == 0:
            print("No hay productos cargados")
        else:
            for producto in productos:
                print(f"Nombre: {nombre} /n Categoria: {categoria} /n Precio: {precio}")
                numero = numero + 1

    elif opcion == "3":
        print("Buscar producto")
        if len(productos) == 0:
            print("No hay productos cargados")
        else:
            busqueda = input("Ingresa el nombre del producto").strip()
            while busqueda == "":
                print("El campo de busqueda no debe vacio")
                busqueda = input("Ingresa el nombre del producto").strip()
            for producto in productos:
                if busqueda.lower() in producto[0].lower():
                    print(f"ID:{numero} /n Nombre: {producto[0]} /n Categoria: {producto[1]} /n Precio: {producto[2]}")
                    encontrado = encontrado + 1
                    numero += 1

            if encontrado == 0:
                print("No se encontraron productos con ese nombre:", busqueda)

    elif opcion == "4":
        print("Eliminar producto")
        if len(productos) == 0:
            print("No hay productos cargados")
        else:
            numero = 1
            for producto in productos:
                print(f"ID:{numero} /n Nombre: {producto[0]} /n Categoria: {producto[1]} /n Precio: {producto[2]}")
                numero = numero + 1

            posicion = input("Numero del producto a eliminar").strip()
            while not posicion.isdigit() or int(posicion) < 1 or int(posicion) > len(productos):
                print(f"Ingresa un numero valido entre 1 y {len(productos)}")
                posicion =input("Numero del producto a eliminar").strip()

            eliminado = productos.pop(int(posicion) -1)
            print(f"Producto '{eliminado[0]}' liminado correctamente")

    elif opcion == "5":
        print("Gracias por usar el sistema! Hasta luego!")
    else:
        print("Opcion invalida: Elegi un nombre del 1 al 5.")