palavra = input("Digite uma palavra:")
letra = input("Digite uma letra:")
contador = 0
for c in palavra:
    if c == letra:
        contador += 1
print("A letra aparece", contador, "vezes.")        