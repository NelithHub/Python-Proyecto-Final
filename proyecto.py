#Datos
nombre_cliente = "      Juan Perez      "
producto = "Dibujo"
monto = 30000
metodo_pago = "efectivo"
telefono = "1234567899"
cupon = "PROMO10"

#Programa
nombre_formateado = nombre_cliente.strip().title()
#print(nombre_formateado)

#Telefono
telefono_valido = telefono.isdigit()

if telefono_valido:
    print("numero de telefono valido")
else:
    print("numero de telefono invalido")



