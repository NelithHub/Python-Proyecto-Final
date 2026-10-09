Inventario_artistica = []
opcion = ""

while opcion != "5":

    print("\n==================================")
    print(" ARTISTICA - INVENTARIO")
    print("====================================")
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

        categoria = input("Ingresa categoria de tu producto: ").strip()
        while categoria == "":
            print("La categoria no puede estar vacio")
            categoria = input("ingresa la categoria del producto: ").strip()

        precio = input("Ingresa el precio del producto, numero entero").strip()
        while not precio.isdigit() or int(precio) == 0:
            print("El precio debe ser un numero entero mayor a 0")
            precio = input("Ingresa el precio del producto, numero entero").strip()


