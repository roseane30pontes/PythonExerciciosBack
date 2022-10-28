unidades=eval(input("Quantas unidades foram comprados?"))
preco=10.0

if (unidades>=11 and unidades<=20):
    preco-=preco*0.1
elif (unidades>20):
    preco-=preco*0.2
else:
    preco=10


total=preco*unidades

print ("O valor total da compra foi de: ",total)
