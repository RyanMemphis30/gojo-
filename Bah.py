import random

# Dicionário de temas e palavras
temas = {
    "animes": ["tate no yuusha no nariagari", "naruto", "tokyo ghoul", "jujutsu kaizen" ],
    "personagens de anime": ["satoru", "yuta", "naofomi", "cain", "subaru"],
    "tecnicas": ["vazio roxo", "escudo da furia", "clones das sombras", "retorno atravez da morte", "muryo kusho"],
    "equipamentos": ["escudo", "catana", "lança", "manopla", "arco"]
}

# Escolhe um tema aleatoriamente
tema_escolhido = random.choice(list(temas.keys()))
palavras = temas[tema_escolhido]
palavra = random.choice(palavras)

tentativas = 6
letras_certas = []
letras_erradas = []

print(f"Tema: {tema_escolhido.capitalize()}")

while tentativas > 0:
    exibicao = ""
    for letra in palavra:
        if letra in letras_certas:
            exibicao += letra
        else:
            exibicao += "_"

    print("\nPalavra:", exibicao)

    if "_" not in exibicao:
        print("Parabéns! Você acertou a palavra:", palavra)
        break

    chute = input("Digite uma letra: ").lower()

    if chute in letras_certas or chute in letras_erradas:
        print("Você já tentou essa letra.")
        continue

    if chute in palavra:
        letras_certas.append(chute)
        print("Boa!")
    else:
        letras_erradas.append(chute)
        tentativas -= 1
        print("Errou! Tentativas restantes:", tentativas)
        print("Letras erradas:", ", ".join(letras_erradas))