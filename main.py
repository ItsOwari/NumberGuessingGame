import random
respostaFinal = int(random.randint(1, 100))


def funcaoJogo(tentativas):
    for n in range(tentativas):
        palpite = int((input("\nInsira seu palpite: ")))
        if palpite == respostaFinal:
            return f"Parabéns, você adivinhou! A resposta era {respostaFinal}"
        elif palpite < respostaFinal:
            print(f"Tente novamente, seu número é maior que {palpite}")
        elif palpite > respostaFinal:
            print(f"Tente novamente, seu número é menor que {palpite}")
    return f"Sinto muito, você perdeu. Seu número era {respostaFinal}..."


print(f"Seja bem vindo(a) ao Acerte o Número™\nEu estou pensando em um número entre 1 e 100 e você deve adivinhá-lo\nPara começar, escolha sua dificuldade!")

dificuldadeJogo = int(input(
    "\n1. Fácil, com 10 tentativas\n2. Médio, com 5 tentativas\n3. Difícil, com 3 tentativas\n"))

tentativas = {1: 10, 2: 5, 3: 3}.get(dificuldadeJogo, 5)

print(funcaoJogo(tentativas))
