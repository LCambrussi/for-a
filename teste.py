import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_dados_desafiante():
    nome_desafiante = input("Digite o nome do Desafiante: ")
    nome_competidor = input("Digite o nome do Competidor: ")
    return nome_desafiante, nome_competidor

def pedir_infos_desafiante():
    palavra_chave = input("Digite a Palavra Chave: ")
    dica1 = input("Digite a Dica 1: ")
    dica2 = input("Digite a Dica 2: ")
    dica3 = input("Digite a Dica 3: ")
    return palavra_chave, dica1, dica2, dica3

def mostrar_infos_competidor(palavra_chave):
    num_letras = len(palavra_chave)
    letras_ocultas = '' num_letras
    print(f"Palavra Chave: {letras_ocultas}")
    escolha = input("Escolha uma opção - Jogar ou Solicitar Dica: ")
    return escolha

def mostrar_dica(dica):
    letra = input(f"Dica: {dica}. Arrisque uma letra: ")
    return letra

def verificar_letra(palavra_chave, letra, letras_reveladas):
    acertou = False
    for i in range(len(palavra_chave)):
        if palavra_chave[i] == letra:
            letras_reveladas[i] = letra
            acertou = True
    return acertou, letras_reveladas

def menu():
    opcao = input("Deseja jogar novamente? (S para Sim / N para Não): ")
    return opcao.lower()
def jogoda_forca():
    nome_desafiante, nome_competidor = pedir_dados_desafiante()
    palavra_chave, dica1, dica2, dica3 = pedir_infos_desafiante()

    limpar_tela()

    letras_reveladas = ['*' for  in range(len(palavra_chave))]
    dicas_utilizadas = 0
    erros = 0

    while True:
        escolha = mostrar_infos_competidor(palavra_chave)

        if escolha.lower() == 'solicitar dica':
            if dicas_utilizadas == 3:
                print("Você já utilizou todas as dicas disponíveis.")
                continue

            dicas_utilizadas += 1
            dica = globals()['dica'+ str(dicas_utilizadas)]
            letra_arriscada = mostrar_dica(dica)
            acertou, letras_reveladas = verificar_letra(palavra_chave, letra_arriscada, letras_reveladas)

            if acertou:
                print("Letra correta!")
            else:
                erros += 1
                print(f"Erro: {erros}")

        elif escolha.lower() == 'jogar':
            letra_arriscada = input("Digite uma letra: ")
            acertou, letras_reveladas = verificar_letra(palavra_chave, letra_arriscada, letras_reveladas)

            if acertou:
                print(f"Letra correta! Palavra: {''.join(letras_reveladas)}")
            else:
                erros += 1
                print(f"Erro: {erros}")

        if erros == 6:
            print("Você perdeu! A palavra chave era: ", palavra_chave)
            break
        if '*' not in letras_reveladas:
            print("Parabéns, você ganhou!")
            break

    opcao = menu()
    if opcao == 's':
        jogo_da_forca()
    else:
        print(f"Até mais, {nome_competidor}!")

jogo_da_forca()