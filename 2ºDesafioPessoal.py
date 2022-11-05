'''Você está trabalhando para uma empresa que fornece materiais escolares e precisa da sua ajuda para entrar no mundo digital. Como primeira atividade, você identificou que não existe uma funcionalidade que é muito importante para a empresa ter mais controle sobre os valores dos produtos vendidos. Esta funcionalidade consiste em descobrir o maior e o menor valor dos produtos vendidos em um período de tempo, para cada vendedor.

Os valores das vendas que devem ser consideradas podem variar entre 20 e 500 reais e estão agrupados por vendedores. Além disso, deve-se ignorar as devoluções, que estão indicadas com o valor 0.

A sua função/método deverá receber uma lista vendas agrupadas por vendedores, (e.g. [[200, 100], [300]]) e retornar um array onde a primeira posição contém o menor valor e a segunda posição o maior valor (e.g. [100, 300]).

Mas preste atenção! Algum vendedor pode não ter realizado vendas no período.'''


def retorna_menor_e_maior_valor_de_vendas(ticket):
    lista = ticket
    novalista = []
    for i in lista:
        quantidadevendas = len(i)
        listaordem = sorted(i)
        menorvalor = 0
        maiorvalor = 0

        for item in listaordem:
            if (item >= 20 and menorvalor == 0):
                menorvalor = item

            if (item >= 20 and item <= 500 and item > maiorvalor):
                maiorvalor = item

        if (menorvalor == 0 and maiorvalor == 0):
            minilista = []
        else:
            minilista = [menorvalor, maiorvalor]

        novalista.append(minilista)

    return novalista
