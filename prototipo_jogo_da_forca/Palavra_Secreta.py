class PalavraSecreta:
    def __init__(self, palavra):
        self.palavra = palavra  # Armazena a palavra secreta
        self.letras_acertadas = []  # Lista vazia para armazenar letras acertadas


    def tentar_letra(self, letra):
        # Verifica se a letra está na palavra
        if letra in self.palavra:
            # Se ainda não acertou essa letra antes
            if letra not in self.letras_acertadas:
                self.letras_acertadas.append(letra)
                return True  # Acertou a letra
            else:
                return False  # Letra repetida (já acertou antes)
        else:
            return False  # Errou a letra


    def mostrar(self):
        # Mostra a palavra com as letras acertadas, as outras ficam com "_"
        resultado = "" #uma palavra vazia.
        for letra in self.palavra:
            if letra in self.letras_acertadas:
                resultado += letra + " "  # o simbolo + está concatenando o que estáno resultado mais a letra atual digita pelo usuário
            else:
                resultado += "_ "
        return resultado.strip() #Ele remove espaços em branco extras no começo e no final de uma palavra ou frase.

    def completa(self):
        # Verifica se todas as letras da palavra já foram acertadas
        for letra in self.palavra:
            if letra not in self.letras_acertadas:
                return False  # ainda falta acertar alguma letra
        return True  # palavra completa
    
