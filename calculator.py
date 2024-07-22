while True:
    print("\n")

    # Função para solicitar um número e tratar entradas inválidas
    def request_number(message):
        while True:
            try:
                return float(input(message))
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

    # Solicita os números e a operação
    number_1 = request_number("Digite o primeiro número: ")
    number_2 = request_number("Digite o segundo número: ")
    operation = input(
        "Digite a operação (+, -, *, /) ou 'sair' para encerrar: "
    )

    if operation == "sair":
        break

    # Inicializa a variável de resultado como nula
    result = None

    try:
        # Realiza a operação de adição
        if operation == "+":
            result = number_1 + number_2

        # Realiza a operação de subtração
        elif operation == "-":
            result = number_1 - number_2

        # Realiza a operação de multiplicação
        elif operation == "*":
            result = number_1 * number_2

        # Realiza a operação de divisão
        elif operation == "/":
            # Trata a divisão por zero
            if number_2 == 0:
                print("\nErro: Divisão por zero não é permitida.")
                continue
            result = number_1 / number_2

        else:
            print("\nOperação inválida. Por favor, tente novamente.")
            continue

        # Verifica se o resultado é inteiro e exibe o tipo apropriado
        if result is not None:
            if result.is_integer():
                print("\n")
                print(f"Resultado: {int(result)}")
            else:
                print("\n")
                print(f"Resultado: {result}")

    # Trata o erro de overflow (resultado muito grande)
    except OverflowError:
        print("\nErro: O resultado é muito grande para ser exibido.")
