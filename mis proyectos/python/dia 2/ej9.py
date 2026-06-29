agenda={
    "manzana": 100,
    "banana" : 50,
    "naranja" : 80,
}
ca = input ("di el nombre de la fruta que quieras")
if ca == "manzana":
   c=int(input("dime cuantos kilos quieres"))
   print("tu precio es",c*agenda["manzana"])
elif ca == "banana":
   ce=int(input("dime cuantos kilos quieres"))
   print("tu precio es",agenda["banana"]*ce)
elif ca == "naranja":
   cf=int(input("dime cuantos kilos quieres"))
   print("tu precio es",agenda["naranja"]*cf)
else:
   print ("no tengo esta fruta")