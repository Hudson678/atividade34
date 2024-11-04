numeros = []

for i in range(5):
    numero = int(input(f"digite um numero inteiro: "))
    numeros.append(numero)


for p, numero in enumerate(numeros):
    print(f"Número na posição {p}: {numero}")
