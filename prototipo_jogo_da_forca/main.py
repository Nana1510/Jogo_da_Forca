from JogodaForca import JogoDaForca  # Importa a classe principal do jogo

# Função para escolher o tema do jogo
def escolher_tema():
    print("-----Seja Bem Vindo ao Jogo Da Forca!!!!-----\n")  # Mensagem de boas-vindas
    print("Escolha um tema e digite o número:\n")  # Orienta o jogador
    print("1 - Linguagens de Programação")  # Opção 1
    print("2 - Conceitos de Programação")   # Opção 2
    print("3 - Ferramentas de Programação \n")  # Opção 3
    
    tema = input("Digite o número do tema (1, 2 ou 3):\n ")  # Lê a escolha do jogador
    
    # Verifica qual opção o jogador escolheu
    if tema == '1':
        return "Linguagens de Programação"
    elif tema == '2':
        return "Conceitos de Programação"
    elif tema == '3':
        return "Ferramentas de Programação"
    else:
        print("Opção inválida. Tente novamente.")  # Mensagem de erro
        return escolher_tema()  # Chama a função novamente até a escolha ser válida

# Função principal do jogo
def jogar():
    tema = escolher_tema()  # Pede para o jogador escolher o tema
    jogo = JogoDaForca(tema)  # Cria o jogo com o tema escolhido
    print(f"\nVocê escolheu o tema: {tema}\n")  # Mostra o tema escolhido

    while True:  # Loop principal do jogo
        print("\nPalavra:", jogo.mostrar_palavra())  # Mostra a palavra com letras descobertas e traços
        print(jogo.desenhar())  # Desenha a forca conforme o número de erros
        print(f"Tentativas restantes: {jogo.tentativas}")  # Mostra quantas tentativas ainda restam
        # Mostra as letras já tentadas ou "Nenhuma" se for a primeira vez
        print(f"Letras já chutadas: {', '.join(jogo.letras_chutadas) if jogo.letras_chutadas else 'Nenhuma'}")
        
        letra = input("Digite uma letra: ").lower()  # Recebe a letra do jogador e converte para minúsculo

        acertou, mensagem = jogo.tentar_letra(letra)  # Verifica se a letra está na palavra
        print(mensagem)  # Mostra o resultado da tentativa (Acertou, Errou, etc.)

        # Verifica se o jogador acertou todas as letras (vitória)
        if acertou and jogo.verificar_vitoria():
            print("\n🎉 Você ganhou! Parabéns!")
            print(f"A palavra era: {jogo.palavra_secreta.get_palavra()}")  # Mostra a palavra completa
            break
        # Verifica se o jogador errou todas as tentativas (derrota)
        elif not acertou and jogo.tentativas == 0:
            print("\n💀 Você perdeu!")
            print(f"A palavra era: {jogo.palavra_secreta.get_palavra()}")  # Mostra a palavra correta
            print(jogo.desenhar())  # Mostra a forca completa
            break

# Ponto de entrada do programa (inicia o jogo)
if __name__ == "__main__":
    jogar()  # Chama a função principal para começar