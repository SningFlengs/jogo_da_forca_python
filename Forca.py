import random
from pathlib import Path
from time import sleep

caminho_lista_palavra = "./palavras.txt"
caminho_lista_rank = "./ranking.txt"

#--------------------PALAVRAS PRÉ-DEFINIDAS--------------------
palavras = [
    "abacaxi", "banana", "cachorro", "dente", "elefante",
    "faca", "girafa", "hotel", "igreja", "janela",
    "kilograma", "laranja", "macaco", "navio", "ovo",
    "pincel", "queijo", "rato", "sapato", "tigre",
    "urso", "vela", "xadrez", "iogurte", "zebra",
    "burro", "cavalo", "dado", "espelho", "foguete",
    "gato", "helicoptero", "isqueiro", "jacare", "ketchup",
    "lampiao", "macarrao", "nariz", "oculos", "piano",
    "queimadura", "raio", "sacola", "tatuagem", "umbigo",
    "violao", "whisky", "xerife", "abelha", "borboleta" ]


def styleprint(txt):
    print("-" * (len(txt) + 6))
    print(f"|  {txt}  |")
    print("-" * (len(txt) + 6))


def gerar_forca(palavra, chutes, chances):
    for letra in palavra:
        if letra in chutes:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chances} chances restantes. \n")


def loading():
    for _ in range(3):
        print(".", end="", flush=True)
        sleep(0.5)


def cadastrar_palavra():
    nova_palavra = input("Digite a nova palavra a ser cadastrada: ")
    with open(caminho_lista_palavra, "a") as lista_palavra:
        lista_palavra.write(nova_palavra + "\n")
        lista_palavra.flush()
    print("Palavra cadastrada com sucesso!")


def procurar_nickname(nickname_usuario, pontos_usuario):
    with open(caminho_lista_rank, "r+") as lista_rank:
        conteudo_lista_rank = lista_rank.readlines()

        nickname_usuario_encontrado = False
        for i, linha in enumerate(conteudo_lista_rank):
            nick, pontos = linha.strip().split()

            if nick == nickname_usuario:    
                nickname_usuario_encontrado = True
                pontos = int(pontos) + pontos_usuario
                conteudo_lista_rank[i] = f"{nick} {pontos}\n"
                

        if not nickname_usuario_encontrado:
            conteudo_lista_rank.append(f"{nickname_usuario} {pontos_usuario}\n")
        
        lista_rank.seek(0)
        lista_rank.writelines(conteudo_lista_rank)
        lista_rank.truncate()


def menu():
    print("\n\n\n")
    styleprint("        JOGO DA FORCA       ")

    styleprint("  Jogar  [1]")
    styleprint(" Ranking  [2]")
    styleprint(" Créditos  [3]")
    styleprint("  Cadastrar Nova Palavra   [4]")
    styleprint(" Sair  [5]")


def antierror_palavra():
    if not Path(caminho_lista_palavra).exists():
        with open(caminho_lista_palavra, "x") as lista_palavras:
            for i in palavras:
                lista_palavras.write(i + "\n")
                lista_palavras.flush()


def antierror_rank():
    if not Path(caminho_lista_rank).exists():
        with open(caminho_lista_rank, "x"):
            pass


while True:

#--------------------VERIFICAÇÃO ANTI-ERROR DE EXISTÊNCIA DAS LISTAS PALAVRA E RANK-------------------- 
    antierror_palavra()
    antierror_rank()

    menu()
    escolha = input()

#--------------------VERIFICAÇÃO DA ESCOLHA DO USUÁRIO NO MENU--------------------
    
#--------------------JOGO PRINCIPAL--------------------
    if escolha == "1":
        
        sortear_palavra = random.randint(0, len(palavras) - 1)
        palavra_forca = str(palavras[sortear_palavra].lower())
        
        chances = 7
        chutes = []
        ganhou = False
        
        nickname_usuario= input("Digite seu Nickname: ").replace(" ", "").lower()
        pontos_usuario = 0


        antierror_rank() 
#--------------------GUARDA O NOME DO PLAYER SE O RANK ESTIVER LIMPO--------------------
        with open(caminho_lista_rank, "r+") as lista_rank:
            lista_rank.seek(0)
            conteudo_lista_rank = lista_rank.readlines()
            
            if len(conteudo_lista_rank) == 0:
                lista_rank.write(f"{nickname_usuario} {pontos_usuario}\n")

#--------------------LOOP DO JOGO PRINCIPAL--------------------
        while True:
            gerar_forca(palavra_forca, chutes, chances)
            
            chute = input("Faça seu chute: ").lower()
            
#--------------------VERIFICA SE A LETRA JÁ FOI CHUTADA, SE ESTÁ ERRADA OU AMBOS--------------------
            if chute in palavra_forca and chute not in chutes:
                chutes.append(chute)
            elif chute not in palavra_forca and chute not in chutes:
                chutes.append(chute)
                chances -= 1
            elif chute in palavra_forca and chute in chutes:
                print("Você já chutou essa letra, tente outra.")
            elif chute not in palavra_forca and chute in chutes:
                print("Você já chutou essa letra, tente outra.")
            
#--------------------A QUALQUER MOMENTO O USUÁRIO PODE DIGITAR A PALAVRA INTEIRA, SE ESTIVER CERTA O USUÁRIO GANHA--------------------
            if chute == palavra_forca:
                styleprint(f"  Parabéns! Você acertou a palavra: {palavra_forca}")
                pontos_usuario += 1
                antierror_rank()
                procurar_nickname(nickname_usuario, pontos_usuario)             
                break
            
#--------------------O JOGADOR GANHOU O JOGO ATÉ QUE SE PROVE O CONTRÁRIO--------------------
            ganhou = True
           
#--------------------É VERIFICADO SE AO MENOS 1 LETRA DA FORCA AINDA NÃO FOI CHUTADA, CASO SIM, O JOGADOR NÃO GANHOU--------------------
            for letra in palavra_forca:
                if letra.lower() not in chutes:
                    ganhou = False

#--------------------O USUÁRIO GANHA SE A CONDIÇÃO ANTERIOR FOR SATISFEITA, PERDE SE AS CHANCES CHEGAREM A 0--------------------
            if chances == 0 or ganhou:
                if ganhou:                    
                    styleprint(f"  Parabéns! Você acertou a palavra: {palavra_forca}  ")
                    pontos_usuario += 1
                    procurar_nickname(nickname_usuario, pontos_usuario)
                    break
                else:
                    styleprint(f"  Suas chances acabaram! A palavra era: {palavra_forca}  ")
                    break
        loading()
  
#--------------------RANKING--------------------
    elif escolha == "2":
        
        print("\n\n\n")
        styleprint("       RANKING       ")
        

        antierror_rank()

#--------------------A LISTA_RANK É LIDA--------------------
        with open(caminho_lista_rank, "r") as lista_rank:
            conteudo_lista_rank = lista_rank.readlines()
            linha_lista = []

#--------------------SE LISTA ESTIVER VAZIA É RETORNADA UMA MENSAGEM--------------------
#--------------------SE TIVER CONTÉUDO NA LISTA ELE É EMPRIMIDO UTILIZANDO STYLEPRINT--------------------
            if len(conteudo_lista_rank) == 0:
                print("Não existe registro de rank para este jogo.")
            else:
                for linha in conteudo_lista_rank:
                    nick, pontos = linha.strip().split()
                    linha_lista.append((nick, int(pontos)))
#--------------------INVERTE A DIREÇÃO PADRÃO DA LISTA PARA DECRESCENTE--------------------
                linha_lista_decrescente = sorted(linha_lista, key = lambda x: x[1], reverse=True)
                
                for i, (jogador, pontos) in enumerate(linha_lista_decrescente[:5], 1):
                    styleprint(f" {jogador}: {pontos} ")
                    sleep(0.7)
                    if i == 5:
                        break
        loading()
  
#--------------------CRÉDITOS--------------------
    elif escolha == "3":
        print("\n\n\n")
        styleprint(" CRIADORES: ÍTALO OLIVEIRA & PEDRO ASSUNÇÃO & LUCCAS LINO")
        loading()

#--------------------CADASTRAR PALAVRAS--------------------      
    elif escolha == "4":
        cadastrar_palavra()
        loading()

#--------------------FECHAR JOGO-------------------- 
    elif escolha == "5":
        break
    
    else:
        print("Escolha inválida, escolha uma das opções do menu.")
        loading()
        menu()      