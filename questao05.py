hora = int(input("Digite um número inteiro entre 0 e 23 para representar a hora do relógio: "))
if hora >= 0 and hora < 12:
    print("Agora é de manha!")
elif hora >= 12 and hora < 18:
    print("Agora é de tarde!")
else:
    print("Agora é de noite!")
    