print("Hello, World!")

#Variables

edad=30
nombre = "Emi"
altura = 1.92
es_estudiante = True

#---------------------------------
#Variables con multiples valores

ciudad = "Buenos Aires"

x,y,z = "German",2,True

print(x)

#---------------------------------
#Variables 

contador = 5
contador = 10 #si se agrga un nuevo valor a la variable, se reemplaza el valor anterior con la nueva variable.
contador = contador + 25

print(contador)

#---------------------------------
#Tipos de datos

#30 -> int
#1.92 -> float
#"Emi" -> string (str o cadena de caracteres)
#True -> boolean (bool) solo reconoce un true o false

#clima -> es una variable que no tiene un valor asignado, por lo tanto es de tipo NoneType

print(bool(0)) #--> valor logico de 0 es false
print(bool(1)) #--> valor logico de 1 es true
print(bool("Hola")) #--> valor logico de "Hola" es true
print(bool("")) #--> valor logico de "" es false


clima = "soleado"
#---------------------------------
#Type
#print(type(altura)) #--> type es una funcion que nos permite saber el tipo de dato de la variable que le pasamos como parametro. 

#Concatenacion de variables
edad=str(edad) #--> convertimos la variable edad de int a string, para poder concatenarla con otras variables de tipo string.

print("Mi nombre es", nombre)
print("mi nombre es " + nombre) # el eespacio es una concatenacion de string, si no se pone el espacio, el resultado seria "minombre esEmi"
#print("mi nombre es " + " " +nombre + "y mi edad es " + edad) # no hacer esto, ya que no se puede concatenar un string con un int, para eso se debe convertir el int a string con str()

print("Mi nombre es" + " " + nombre)
print("mi nombre es " + " " +nombre + "y mi edad es " + str(edad))

print(f"Hola Mi nombre es {nombre} y mi edad es {edad}") #--> fstring, es una forma de concatenar variables de diferentes tipos de datos, sin necesidad de convertirlas a string.

#Solicitar datos
# input() --> es una funcion que nos permite solicitar datos al usuario, y devuelve un string con el valor ingresado por el usuario.

#nombre_user = input("ingrese su nombre: ")

#print(f"Hola {nombre_user}, gracias por visitarnos")

edad_user = input("Ingrese su edad: ")

edad_INT = int(edad_user)

anio_nacimiento = 2026 - edad_INT #tiene que ser edad_INT para validar que el valor ingresado por el usuario sea un numero entero, ya que si no se hace esto, el valor ingresado por el usuario sera un string y no se podra realizar la operacion de resta.

print(anio_nacimiento)
