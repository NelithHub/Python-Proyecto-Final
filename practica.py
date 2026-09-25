#numero = int("10")
#print(numero * 2)

#nombre = "Juan"

#edad = 30

#print("Hola,", nombre, "tenés", edad, "años.")

#edad = input("Ingresá tu edad: ")

#edad = int(edad)

#print("Tu edad es:", edad)

#x, y, z = 1, 2, 3

#print(x + y + z)

#edad = "25"

#print(int(edad) + 5)

#clase 4

#edad= 125

#if edad < 15:
#    print("Es menor")
#elif edad >= 13 and edad < 18:
#    print ("Es adolecente")
#elif edad >=18:
#    print("Es adulto")
#else:
#    print("Edad no valida")

#if fruta == "manzana":
#    print("rojo o verde")
#elif fruta == "banana":
#    print("amarillo")
#elif fruta == "naranja":
#    print("anaranjado")
#else:
#    print("Desconocida")


#match fruta:
#    case "manzana":
#        print("rojo o verde")
#    case "banana":
    #        print("amarillo")
#    case "naranja":
#        print("anaranjado")
#    case _:
    #        print("Desconocida")


#len()

##print(len(mensaje)) #--> len() es una funcion que nos permite saber la cantidad de caracteres que tiene un string.

#nombre = input("ingresa tu nombre: ")

#if len(nombre) == 0:
    #print("eldato solicitado no cumple con lo esperado")
#elif len(nombre) > 2:
    #print("su nombre es:", nombre)


# salir_prog =input("ingresa ´salir´ para salir del programa: ").strip().lower()

    #upper()
    #if salir_prog == "salir":
        #print("programa terminado")
#else:
    #print("dsigo preguntado")

#print (mensaje[0])

#nota = 85

#if nota >= 90:

#    print("Excelente.")

#elif nota >= 75:

#    print("Muy bien.")

#else:

#    print("Suficiente.")

#Bucle while 

#contador = 1
#while contador <=5:
#    print(f"Este es el intento numero {contador}")
#    contador +=1 # contador = contador + 1 - (nunca crear un bucle infinito )

#nombre = ""
#while nombre == "":
#    nombre = input("Ingresa tu nombre").strip()
#    if nombre == "":
#        print("El nombre no puede estar vacio. Intenta de nuevo")

##intentos = 0
#max_intentos = 3
#user_correcto = "admin"
#user_encontrado = False

#while intentos < max_intentos and not user_encontrado:
#    user_ingresado = input("Ingrese su usuario: ")

#    if user_ingresado == user_correcto:
#        print("Acceso exitoso")
#        user_encontrado = True
#    else:
#        intentos +=1
#        print("Usuario incorrecto")

#        if intentos < max_intentos:
#            print(f"Te quedan {max_intentos - intentos} intentos")

#if not user_encontrado:
#    print(f"Se agotanron los {max_intentos} intentos. Acceso denegado")


#----------------------------------------------------------------------

# Tipo de datos en listas - se definene entre "[]" y se separan por comas
#lista = ["manzana", "banana", "naranja"]

#lista_num = [10,5,20,7,30,40]

#lista_global = ["ana",True,20,{1,2,3},"12",3.14," "]

#print(lista_global[5])

#print(len(lista_num))

#indice = 0

#while indice < len(lista_num):
#    print(f"indice {indice} --- {lista_num[indice]}")
#    if lista_num[indice] % 2== 0:
#        print(lista_num[indice])

#    indice+=1

#Sentencia Break (rompe el while o fuerza a salir del bucle) y continue (salta a la siguiente iteracion del bucle)

#numero_buscado = 40
#encontrado = False
#while indice < len(lista_num):
#    if lista_num[indice] == numero_buscado:
#        print(lista_num[indice], "encontrado")
#        break

#    print(f"Indice {indice} --- el elemento en ese indice es: {lista_num[indice]}")
#    indice +=1

#    temperaturas = [18, 19, 21, -999, 23, 25, 27, 30, 32, 35, 38, 31,
#                   39, -999, 34, 30, 28, 26, 24, 22, 21, 20, -999, 18]

#indice = 0
#suma = 0
#cantidad_validas = 0
#alerta_activada = False

#EJERCICIO - CLASE 05: BUCLES WHILE + LISTAS

#Consigna:
#Una estación meteorológica registró la temperatura de cada hora del día
#en la siguiente lista. Algunos sensores fallaron y guardaron el valor
#-999 en vez de una temperatura real.

#    temperaturas = [18, 19, 21, -999, 23, 25, 27, 30, 32, 35, 38, 41,
#                    39, -999, 34, 30, 28, 26, 24, 22, 21, 20, -999, 18]

#Escribí un programa que, usando while (nada de for):
 
#1. Recorra la lista con un índice y muestre cada temperatura junto
#   con la hora que representa (la posición 0 es la hora 0, etc.).

#2. Ignore con "continue" los valores -999 (dato inválido), mostrando
#   un aviso distinto para esos casos.

#3. Vaya acumulando la suma de las temperaturas válidas y cuente
#   cuántas son, para poder calcular el promedio al final.

#4. Corte el recorrido con "break" apenas encuentre una temperatura
#   mayor o igual a 40°C, mostrando en qué hora ocurrió (alerta de
#   calor extremo). Si esto pasa, no se debe mostrar el promedio,
#   porque el recorrido quedó incompleto.

#5. Si el recorrido termina sin activarse la alerta, mostrar el
#   promedio de las temperaturas válidas.

#6. Después, armar un menú con "while True:" que le permita al
#   usuario consultar la temperatura de una hora específica (pidiendo
#   un número de 0 a 23) tantas veces como quiera, hasta que ingrese
#  -1 para salir. Acá "while True:" es la opción correcta porque no
#  sabemos de antemano cuántas consultas va a hacer el usuario antes
#   de decidir salir.


#temperaturas = [18, 19, 21, -999, 23, 25, 27, 30, 32, 35, 38, 31,
#                    39, -999, 34, 30, 28, 26, 24, 22, 21, 20, -999, 18]

#indice = 0
#suma = 0
#cantidad_validas = 0
#alerta_activada = False


#while indice < len(temperaturas):
#    temperatura = temperaturas[indice]
    
#    if temperatura == -999:
#        print(f"Hora {indice}: dato invalido, se ignora")
#        indice+=1
#        continue
    
#    if temperatura >= 40:
#        print(f"Hora {indice}: {temperatura}°C Alerta de calor extremo")
#        alerta_activada = True
#        break
    
    # suma = suma + temperatura
#    suma += temperatura 
#    cantidad_validas +=1
#    indice+=1
    

#if alerta_activada:
#    print(f"El recorrido se detuvo por la alerta, no se calcula el promedio")
#else:
#    promedio = suma / cantidad_validas
#    print(f"promedio de temperaturas validas: {promedio:.2f}°C")
    

#-----------------------------------------------------

#print("Consulta de temparatura por hora (-1 para salir)")
#while True:
#    hora = int(input("Ingresa una hora (0-23) o -1 para salir"))
    
#    if hora == -1:
#        print("Hasta luego!")
#        break
    
#    if hora < 0 or hora > 23:
#        print("Hora invalida, tiene que estar entre 0 y 23")
#        continue
    
#    print(f"Tempratura registrada a la hora {hora}: {temperaturas[hora]}°C")

#------------------------------------------------------------------------------------------------

#Clase 06 - Listas y bucles (for)

#For variable in secuencia:
#   print()

#productos = ["manzana", "banana", "naranja", "pera"]

#for producto in productos:
#    print(producto)

#productos = ["manzana", "naranjas", "anana", "bebidas", ["banannas", "Ecuador", "P&G"]]

#for producto in productos:
#    print (producto)
#    if isinstance(producto,list):
#        for prod in producto:
#            print(prod)

#for i in range(len(productos)):
#    print(f"indice {i} - elemento: {productos[i]}")


#range(inicio,fin, paso) genera saltando lugares

#for i in range(10,0,-1):
#    print(i)

#CLASE PRACTICA 06

# =====================================================================
#                 CONSIGNA: SISTEMA DE GESTIÓN DE BIBLIOTECA
# =====================================================================
#
# Una biblioteca de barrio necesita un pequeño programa para llevar el
# registro de sus libros. Desarrollá un programa en Python que cumpla
# con los siguientes requerimientos:
#
# * Ingreso de datos de libros: El sistema debe permitir ingresar los
#   datos básicos de los libros: título, autor y año de publicación
#   (solo números). Estos datos deben almacenarse en una lista, donde
#   cada libro sea representado como una sublista de tres elementos
#   (título, autor y año).
#
# * Visualización de libros registrados: El programa debe incluir una
#   funcionalidad para mostrar en pantalla todos los libros ingresados.
#   La información debe presentarse de manera ordenada y legible, con
#   cada libro numerado. Si no hay libros cargados, debe informarlo.
#
# * Búsqueda de libros: El sistema debe permitir buscar libros por su
#   título, sin importar mayúsculas o minúsculas. Si encuentra
#   coincidencias, debe mostrar la información completa de los libros
#   que coincidan. Si no hay coincidencias, debe informar que no se
#   encontraron resultados.
#
# * Menú principal: Todas las opciones deben ofrecerse desde un menú que
#   se repita hasta que el usuario elija la opción "Salir".

#     print("========== BIBLIOTECA ==========")
#     print("1. Ingresar libro")
#     print("2. Mostrar libros registrados")
#     print("3. Buscar libro por título")
#     print("4. Salir")
#     print("================================")


#libros = []
#opcion = ""

#while opcion != "4":
#    print("========== BIBLIOTECA ==========")
#    print("1. Ingresar libro")
#    print("2. Mostrar libros registrados")
#    print("3. Buscar libro por título")
#    print("4. Salir")
#    print("================================")

#    opcion = input("Seleccione una opción: ").strip()

    #--------------Ingreso-----------------
#    if opcion == "1":
#        titulo = input("Titulo: ").strip()
#        while titulo == "":
#            print("El titulo no puede estar vacio")
#            titulo = input("Titulo: ").strip()

#        autor = input("Autor: ").strip()
#        while autor == "":
#            print("El autor no puede estar vacio")
#            autor = input("autor: ").strip()

#        anio = input("Año: ").strip()
#        while not anio.isdigit():
#            print("El año no puede estar vacio")
#            anio = input("Año: ").strip()

#        libros = libros + [[titulo, autor, anio]]
#        print("Libro registrado con exito")

    #Mostrar los libros ----------
#    elif opcion == "2":
#        if libros == []:
#            print("No Hay libros en la lista")
#        else:
#            numero = 1
#            for libro in libros:
#                print(numero, "Titulo", libro[0].upper(), "| Autor:", libro[1].title(), "| Año", libro[2])
#                numero += 1
#            print("---------------------")

    #Buscar libro ----------------
#    elif opcion == "3":
#        if libros == []:
#            print("No Hay libros en la lista")
#        else:
#            buscado = input("Ingresa el titulo a buscar: ").strip().lower()
#            encontrado = 0
#            for libros in libros:
#                if buscado in libro[0].lower():
#                    encontrado = encontrado + 1
#                    print("Titulo", libro[0].upper(), "| Autor:", libro[1].title(), "| Año", libro[2])
#            if encontrado == 0:
#                print("No se encontraron resultados")
#            else:
#                print("Se encontraron", encontrado, "coincidencia/s")
        

    #Despedida -------------------
#    elif opcion == "4":
#        print("Gracias por usar el sistema de la biblioteca")

#    else:
#        print("Opcion invalida. Elegi una opción del 1 al 4")

#CLASE 07
#listas y duplas

#productos = ["pan", "leche", "queso", "yogurt", "manteca"]

#print(productos[-2])

#APPEND

#lista.append(elemento_agregar)

#productos.append("yerba")

#print(productos)

#lista(lista_productos)
#lista_productos = []
#
#continuar = "si"

#while continuar == "si":
#    nombre = input("Emi")
#    precio = input("36")
#    categoria = input("master")

#    lista_productos.append([nombre, precio, categoria])
#    continuar = input("Queres agregar otro producto? si/no").strip().lower()


#print(lista_productos)
#print(lista_productos[0])

#for producto in lista_productos:
#    print(producto[0])
#    print(producto[1])
#    print(producto[2])

#lista = [["Emi", "36", "Master"], ["Santi", "35", "consulta"]]

#print(lista[1][1])

#lista[1][1] = "36"

#print(lista)

#Remove
#busca y elimina un valor especifico

#lista.remove(valor_a_eliminar)

#productos = ["pan", "leche", "queso", "yogur", "manteca", "pan", "pan"]

#productos.remove("pan")

#while "pan" in productos:
#    productos.remove("pan")

#print(productos.count("pan"))

#while productos.count("pan") > 1:
#    productos.remove("pan")

#print(productos)

#pop(indice)

#productos.pop(1)

#print(productos)

#lista_num = [5,6,9,1,2,3,4]

#lista_num.sort(reverse=True)
#print(lista_num)

#productos.sort()
#print(productos)


#print(productos.index("manteca"))
#productos.insert(2, "dulce de leche")

#print(productos)



#Tuplas (similares a las listas, todo lo que se pueden hacer en las listas con las tuplas no)
#()

tupla1 = (10,20,30, [])

tupla2 = 40,50,60

#las tuplas pueden guardar todo tipo de datos (numeros enteros, decimales, etc.) pero no se puede modificar dentro de la tupla solo se puede buscar

#nombre = input("nombre")
#precio = input("precio")
#categoria = input("categoria")

#tupla_prod = (nombre, precio, categoria)
#tupla1[3].append("Emi")
#print(tupla1[2])
#tupla1[2] = 50
#print(tupla1[2])


lista_tupla = list(tupla1)
print(lista_tupla)
lista_tupla = tuple(tupla1)
print(lista_tupla)

tupla3 = (1,)