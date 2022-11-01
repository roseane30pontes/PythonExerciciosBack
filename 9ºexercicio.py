def verificaPrimo (numero):
    metade=numero//2
    if (numero<2):
        return False

    while (metade>1):
        if (numero%metade==0):
            return False
        metade-=1
    return True

def imprimeresultado (num,result):
        mensagem=f"O número {num} não é primo"
        if(result):
            mensagem=f"O número {num} é primo"
        return mensagem

eprimo = eval(input("Digite o número a ser verificado:"))
resultado = verificaPrimo(eprimo)
impressao=imprimeresultado(eprimo,resultado)

print(impressao)




