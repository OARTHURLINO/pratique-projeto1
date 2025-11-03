print("CALCULADORA \n")

pergunta = 1

while pergunta == 1:
    valor1 = float(input("Por favor, digite o primeiro valor: \n"))
    valor2 = float(input("Por favor, digite o segundo valor: \n"))

    operacao = int(input("\n Escolha uma operação: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n"))

    if operacao == 1:
        resultado = valor1 + valor2
    elif operacao == 2:
        resultado = valor1 - valor2
    elif operacao == 3:
        resultado = valor1 * valor2
    elif operacao == 4:
        resultado = valor1 / valor2
    else:
        print("Operação inválida!")
        continue  # volta para o início do loop

    print(f"Resultado: {resultado:.2f}")

    pergunta = int(input("\n Deseja fazer mais alguma operação? \n 1 - Sim \n 2 - Não \n"))
