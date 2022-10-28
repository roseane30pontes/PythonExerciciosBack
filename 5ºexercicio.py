list=[]
lista=eval(input("Escreva os números da sua lista:"))

soma=0
for num in lista:
    if (num%2==0):
        soma+=num
    else:
        pass
print ("O valor da soma dos pares foi: ",soma)
