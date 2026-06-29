saldo = 1000
pin= 1234
def verificar_pin(pin_usuario):
    if pin_usuario==pin:
        return True
    else:
        return False
def retirar(cantidad):
    if cantidad<saldo:
        s= saldo-cantidad
        print("tu saldo es", s)
    else:
        print("tu saldo es insuficiente")
pin_usu=int(input("ingresa tu pin"))
if verificar_pin(pin_usu):
    try:
        monto=int(input("cuanto queres retirtar"))
        retirar(monto)
    
    except ValueError:
        print("Error:ingrese pin valido")
else:
    print("pin incorrecto")








