import random
respostaFinal = int(random.randint(1, 100))


def funcaoJogo(tentativas):
    for n in range(tentativas):
        palpite = int((input("Insira seu palpite: ")))
        if palpite == respostaFinal:
            return f"Parabéns, você adivinhou! A resposta era {respostaFinal}"
        elif palpite < respostaFinal:
            print(f"Tente novamente, seu número é maior que {palpite}")
        elif palpite > respostaFinal:
            print(f"Tente novamente, seu número é menor que {palpite}")
    return f"Sinto muito, você perdeu. Seu número era {respostaFinal}..."


dificuldadeJogo = int(input(
    f"Seja bem vindo(a) ao Acerte o Número™\nPrimeiramente, escolha sua dificuldade!\n1. Fácil, com 10 tentativas\n2. Médio, com 5 tentativas\n3. Difícil, com 3 tentativas\n"))

tentativas = {1: 10, 2: 5, 3: 3}.get(dificuldadeJogo, 5)

print(funcaoJogo(tentativas))
