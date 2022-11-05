def ultima_parada(combustivel, consumo, postos_de_gasolina):
    autonomia = combustivel * consumo
    postos2 = sorted(postos_de_gasolina)


    if (len(postos_de_gasolina) == 0):
        return -1
    else:
        postoMaisDistante = 0

    for i in postos2:
        if (autonomia > i):
            postoMaisDistante = i
    else:
        return postoMaisDistante


combustivel = 2
consumo = 8
postos = [2, 15, 22, 10.2]

abastecimento = ultima_parada(combustivel, consumo, postos)

print(f"O posto mais distante possível para abastecimento está a {abastecimento} quilometros.")