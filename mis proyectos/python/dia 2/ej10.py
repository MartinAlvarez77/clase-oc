contra_secreta = "eloy"
ver=True
c = input("dime la contraseña")
while ver: 
    if c==contra_secreta:
        ver=False
        print("¡binevenido!")
    else:
        c = input("dime la contraseña")