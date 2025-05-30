
import random


facil = ["php", "sql", "java", "html", "ruby", "perl", "bash", "css", "c", "r"]
medio = ["python", "golang", "kotlin", "csharp", "shell", "scala", "groovy", "swift"]
dificil = ["typescript", "javascript", "objectivec", "assembly", "fortran", "visualbasic", "matlab", "cobol", "powershell", "delphi"]


forca = [
    """
     ------
     |    |
          |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    =========
    """
]


jogando = True
while jogando:
    inicio = input('Bem-vindo ao jogo da forca! Digite "COMEÇAR" para iniciar:\n').strip().upper()
    if inicio != "COMEÇAR":
        print('Digite corretamente "COMEÇAR" para iniciar.')
        continue

    nivel = ""
    while nivel not in ["1", "2", "3"]:
        nivel = input('Escolha a dificuldade:\n1 - Fácil\n2 - Médio\n3 - Difícil\n')
        if nivel not in ["1", "2", "3"]:
            print("Opção inválida. Tente novamente.")

    if nivel == "1":
        palavras = facil
        tentativas = 6
    elif nivel == "2":
        palavras = medio
        tentativas = 5
    elif nivel == "3":
        palavras = dificil
        tentativas = 4

    palavra = random.choice(palavras).upper()
    acertos = ["_"] * len(palavra)
    letras_usadas = set()
    erros = 0
    pontos = 0

    print("\nPalavra: " + " ".join(acertos))

    while erros < tentativas and "_" in acertos:
        print(forca[erros])
        entrada = input('\nDigite uma letra ou a palavra inteira. Para dica, digite "DICA":\n').strip().upper()

        if entrada == "DICA":
            print("💡 Dica: É uma linguagem de programação!")
            continue

        if len(entrada) > 1:
            if entrada == palavra:
                acertos = list(palavra)
                pontos += 50  # bônus
                break
            else:
                print("Palavra errada! Você perdeu o jogo.")
                erros = tentativas
                break

        if entrada in letras_usadas:
            print("Você já usou essa letra!")
            continue

        letras_usadas.add(entrada)

        if entrada in palavra:
            for i in range(len(palavra)):
                if palavra[i] == entrada:
                    acertos[i] = entrada
            pontos += 10
            print(f"✅ Letra correta! Pontos: {pontos}")
        else:
            erros += 1
            print(f"❌ Letra errada! Tentativas restantes: {tentativas - erros}")

        print("Letras usadas:", ", ".join(sorted(letras_usadas)))
        print("Palavra: " + " ".join(acertos))

    if "_" not in acertos:
        print("\n🎉 Parabéns! Você acertou a palavra:", palavra)
    else:
        print(forca[erros])
        print(f"\n❌ Você perdeu! A palavra era: {palavra}")

    print(f"🏅 Pontuação final: {pontos} pontos")

    continuar = input('\nDeseja jogar novamente? (S/N):\n').strip().upper()
    if continuar != "S":
        print("Obrigado por jogar! Até a próxima.")
        jogando = False
