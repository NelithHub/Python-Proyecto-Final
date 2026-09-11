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

lista_num = [10,5,20,7,30,40]

#lista_global = ["ana",True,20,{1,2,3},"12",3.14," "]

#print(lista_global[5])

#print(len(lista_num))

indice = 0

while indice < len(lista_num):
    print(f"indice {indice} --- {lista_num[indice]}")
    if lista_num[indice] % 2== 0:
        print(lista_num[indice])

    indice+=1

#Sentencia Break (rompe el while o fuerza a salir del bucle) y continue (salta a la siguiente iteracion del bucle)

numero_buscado = 40
encontrado = False
while indice < len(lista_num):
    if lista_num[indice] == numero_buscado:
        print(lista_num[indice], "encontrado")
        break

    print(f"Indice {indice} --- el elemento en ese indice es: {lista_num[indice]}")
    indice +=1