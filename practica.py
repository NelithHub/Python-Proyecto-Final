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

edad = "25"

print(int(edad) + 5)

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

if fruta == "manzana":
    print("rojo o verde")
elif fruta == "banana":
    print("amarillo")
elif fruta == "naranja":
    print("anaranjado")
else:
    print("Desconocida")


match fruta:
    case "manzana":
        print("rojo o verde")
    case "banana":
        print("amarillo")
    case "naranja":
        print("anaranjado")
    case _:
        print("Desconocida")


#len()

mensaje ="hola"
print(len(mensaje)) #--> len() es una funcion que nos permite saber la cantidad de caracteres que tiene un string.

nombre = input("ingresa tu nombre: ")

if len(nombre) == 0:
    print("eldato solicitado no cumple con lo esperado")
elif len(nombre) > 2:
    print("su nombre es:", nombre)


    salir_prog =input("ingresa ´salir´ para salir del programa: ").strip().lower()

    #upper()
    if salir_prog == "salir":
        print("programa terminado")
else:
    print("dsigo preguntado")

print (mensaje[0])