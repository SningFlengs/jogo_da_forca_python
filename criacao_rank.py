from pathlib import Path


def criar():
    caminho = "./rank.txt"
        
    if not Path(caminho).exists():
        with open(caminho, "x"):
            pass

criar()


#pede nome do usuario
nome = "user"
pontuacao = 0


nome = str(input("Digite seu nome: "))

with open("rank.txt", "r+") as ranklist:
    cont_ranklist = ranklist.readlines()
    
    if len(cont_ranklist) == 0:
        ranklist.write(f"{nome} {pontuacao}")

#partida encerra e o player ganhou

pontuacao += 1

with open("rank.txt", "r+") as ranklist:
    cont_ranklist = ranklist.readlines()

    encontrado = False
    for i, linha in enumerate(cont_ranklist):
        nick, ponto = linha.strip().split()

        if nick == nome:    
            ponto = int(ponto) + pontuacao
            cont_ranklist[i] = f"{nick} {ponto}\n"
            encontrado = True

    if not encontrado:
        cont_ranklist.append(f"{nome} {pontuacao}\n")
    
    ranklist.seek(0)
    ranklist.writelines(cont_ranklist)
    ranklist.truncate()

