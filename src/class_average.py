# Registro de notas e cálculo da média
def calcular_media_turma():
    notas = []
    while True:
        nota = input("Digite a nota do aluno (ou 'media' para calcular a média das notas): ")
        if nota.lower() == "media":
            break
        try:
            notas.append(float(nota))
        except ValueError:
            print("Por favor, insira um número válido.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Média da turma: {round(media, 2)}")
    else:
        print("Nenhuma nota foi registrada.")

calcular_media_turma()