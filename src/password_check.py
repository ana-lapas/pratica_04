def verificar_senha():
    while True:
        senha = input("Digite uma senha sabendo que deve ter pelo menos 8 caracteres e pelo menos um número: ")

        if len(senha) < 8:
            print("A senha deve ter pelo menos 8 caracteres.")
        elif not any(char.isdigit() for char in senha):
            print("A senha deve conter pelo menos um número.")
        else:
            print("Senha válida!")
            break

verificar_senha()