from Palavra_Secreta import PalavraSecreta

class JogoDaForca:

    desenhar_forca = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ---------
        """
    ]

    def __init__(self, palavra):
        self.palavra_secreta = PalavraSecreta(palavra)  # Inicializa a palavra secreta.
        self.tentativas = 6  # Número máximo de tentativas erradas.
        self.letras_chutadas = []  # Lista para guardar letras já tentadas.

    def tentar_letra(self, letra):
        letra = letra.lower()

        if letra in self.letras_chutadas:
            return False, "Letra já chutada"  # Retorna erro se a letra já foi tentada.

        self.letras_chutadas.append(letra)  # Adiciona a letra na lista de tentativas.

        if self.palavra_secreta.tentar_letra(letra):  # Verifica se a letra foi correta.
            if self.verificar_vitoria():  # Verifica se o jogador venceu.
                return True, "Ganhou"
            return True, "Acertou a letra"
        else:
            self.tentativas -= 1  # Diminui uma tentativa.
            if self.tentativas == 0:  # Se as tentativas acabaram, o jogador perde.
                return False, "Perdeu"
            return False, "Errou a letra"

    def mostrar_palavra(self):
        return ' '.join([letra if letra in self.palavra_secreta.letras_acertadas else '_' for letra in self.palavra_secreta.palavra])

    def verificar_vitoria(self):
        return all(letra in self.palavra_secreta.letras_acertadas for letra in self.palavra_secreta.palavra)

    def desenhar(self):
        return self.desenhar_forca[6 - self.tentativas]  # Usa o número de tentativas restantes para desenhar a forca.
