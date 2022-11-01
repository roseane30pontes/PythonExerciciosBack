import math

a=eval(input("Digite ovalor de A: "))
b=eval(input("Digite o valor de B: "))
c=eval(input("Digite o valor de C: "))

def calculoDelta (A,B,C):
    delta=B**2-4*A*C
    return delta

def calcraiz (a,b,delt):
    if (delt < 0):
        resultado="A equação não possui raizes nos números reais."
    elif (delt==0):
        x=-b/2*a
        resultado= f"A equação possui apenas a raiz{x}"
    else:
        x1=(-b+math.sqrt(delt))/(2*a)
        x2=(-b-math.sqrt(delt))/(2*a)
        resultado= f"As raízes da equação são: {x1} e {x2}"
    return resultado

delta=calculoDelta(a,b,c)
raizes=calcraiz(a,b,delta)

print(raizes)

