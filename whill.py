while True:
    print("\n==== CONVERSOR ======")
    print("1- converter Celsius - Fahrenheit")
    print("2- converter Fahrenheit - Celsius")
    print("3- converter Metros - Centimetros")
    print("4- converter Centimetros - Metros")
    print("0- Sair")
    opção = input("Escolha uma opção (1/2/3/4/0):")
    if opção == '0':
        print("Saindo do conversor. Até mais!")
        break
    elif opção == 1:
        c = float(input("Digite a temperatura em Celsius:"))
        f = c * 1.8 + 32
        print(f"{c}°C é igual a {f} °F")
    elif opção == 2:
        f = float(input("Digite a temperatura em Fahrenheit:"))    
        c = (f-32) / 1.8
        print(f"{f}°F é igual a {c}°C")
    elif opção == '3':
        m = float(input("Digite a medida em metros:"))  
        cm = m * 100
        print(f"{m} metros é igual a {cm} centímetros")  
    elif opção == '4':
        cm = float(input("Digite a medida em centímetros:"))   
        m = cm / 100
        print(f"{cm} centímetros é igual a {m} metros")
    else:
        print("Opção inválida. Tente novamente")     

