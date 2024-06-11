numero = int(input("Digite um número para a tabuada de multiplicação: "))
for i in range(1, 11):
    produto = numero * i
    print(f"{numero} x {i} = {produto}")
