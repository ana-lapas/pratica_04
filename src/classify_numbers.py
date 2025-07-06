def classify_numbers():
    evens = 0
    odds = 0
    print("Olá! Bom-vindo ao classificador de Números!")
    while True:
        entry = input("Digite um número (ou 'fim' para sair): ")
        if entry.lower() == "fim":
            break
        try:
            number = int(entry)
            if number % 2 == 0:
                evens += 1
            else:
                odds += 1
        except ValueError:
            print("Por favor entre um número válido.")

    print(f"Total de números pares: {evens}")
    print(f"Total de números ímpares: {odds}")

classify_numbers()