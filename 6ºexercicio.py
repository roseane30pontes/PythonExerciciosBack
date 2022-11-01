lista=eval(input("digite os números da sua lista: "))

def menorNumero (listalocal):
    menor=listalocal[0]
    for i in listalocal:
        if (i<menor):
            menor=i
    return menor

valormaisbaixo = menorNumero(lista)
print("O menor número da lista é:", valormaisbaixo)
