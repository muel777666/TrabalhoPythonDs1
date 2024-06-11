def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Não é possível dividir por zero."

def calculadora():
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))

    print("Soma:", soma(num1, num2))
    print("Subtração:", subtracao(num1, num2))
    print("Multiplicação:", multiplicacao(num1, num2))
    print("Divisão:", divisao(num1, num2))

calculadora()
