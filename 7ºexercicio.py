lista=eval(input("Digite os números da sua lista: "))

def adicaopar (listalocal):
    soma=0
    for i in listalocal:
        if (i%2==0):
            soma+=i
    return soma

somapar=adicaopar(lista)

print ("A soma dos pares da lista é: ", somapar)