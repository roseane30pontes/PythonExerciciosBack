nota=eval(input('Digite sua nota: '))

if (nota>=7):
    situacao='Aprovado'
elif (nota>=5):
    situacao='Em recuperação'
else:
    situacao="Reprovado"

print ("O aluno está:",situacao)