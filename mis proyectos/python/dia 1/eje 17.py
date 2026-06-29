numero_secreto = 8
adivina= int(input("adivina el numero"))

if adivina != numero_secreto:
    print("numero equivocado")
elif adivina == numero_secreto:
    print ("adivinaste")