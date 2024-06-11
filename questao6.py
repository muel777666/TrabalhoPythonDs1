nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
if idade >= 16:
    print(f"Parabéns, {nome}! Você pode emitir o seu título de eleitor.")
else:
    print(f"Desculpe, {nome}, você ainda não pode emitir o seu título de eleitor.")
