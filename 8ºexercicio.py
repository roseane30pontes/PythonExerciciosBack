numerofatorial=eval(input("Digite o número: "))

def fatorial(numerofat):

    if (numerofat==1 or numerofat==0):
        multiplicacao=1
    else:
        multiplicacao=1
        for i in range(1,numerofat):
            numeros=numerofat-i
            multiplicacao*=numeros
        multiplicacao*=numerofat

    return multiplicacao

resultado=fatorial(numerofatorial)

print(numerofatorial," fatorial é igual a: ",resultado)



