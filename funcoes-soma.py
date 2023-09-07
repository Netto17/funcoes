import os
stop=False
def soma(a,b): print("o resultado é:",a+b)
def subtracao(a,b): print("o resultado é:",a-b)
def multiplicacao(a,b): print("o resultado é:",a*b)
def divisao(a,b): print("o resultado é:",a/b)
def potencia(a,b): print("o resultado é:", pow(a,b))
while stop==False:
    os.system('cls')
    print("----------Calculadora----------")
    print("1-Soma")
    print("2-Subtração")
    print("3-Multiplicação")
    print("4-Divisão")
    print("5-Potenciação")
    print("-------------------------------")
    op=int(input("Digite a opção escolhida:"))
    n1=int(input("Digite o primeiro valor: "))
    n2=int(input("Digite o segundo valor: "))
    match op:
        case 1: soma(n1,n2)
        case 2: subtracao(n1,n2)
        case 3: multiplicacao(n1,n2)
        case 4:
            if n2!=0:
                divisao(n1,n2)
            else:
                print("Impossivel")    
        case 5: potencia(n1,n2)
    op=input("Pressione qualquer tecla para continuar...")