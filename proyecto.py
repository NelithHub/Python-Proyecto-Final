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

#Como empieza el cupon (Validar)

cupon_valido = cupon.startswith("PROMO") and cupon[-1].isdigit()
termina_en_letra = cupon.endswith(("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"))

#Calculo del envio del producto (montos)

if monto < 10000:
    envio = 1500
elif monto < 30000:
    envio = 800
else:
    envio = 0    

# Calculo de descuento por metodo de pago

match metodo_pago:
    case "efectivo":
        descuento = 0.10
    case "transferencia":
        descuento = 0.05
    case "tarjeta":
        descuento = 0.0
    case _:
        descuento = None

if descuento == None:
    print("X Metodo de pago invalido. No se puede procesar el pedido.")
elif not telefono_valido:
    print(f"X Telefono invalido. {telefono} debe contener numeros")
else:

    if cupon_valido:
        descuento_total = descuento + 0.5
    else:
        descuento_total = descuento

    monto_con_descuento = monto - (monto * descuento_total)
    total_final = monto_con_descuento + envio

    print(f"Cliente: {nombre_formateado}, producto: {producto}, telefono: {telefono}, cupon: {cupon}, monto original: {monto}, descuento total: {descuento_total}, envio: {envio} {'-'*10} Total final: {total_final}")




