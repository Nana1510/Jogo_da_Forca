# PalavraSecreta.py

import random # permite aleatorieadade das palavras

class PalavraSecreta:
    def __init__(self, tema):
        self.temas = {
            "Linguagens de Programação": ["python", "java", "javascript"],
    "Conceitos de Programação": ["variavel", "função", "classe", "objeto", "heranca", "polimorfismo"],
    "Ferramentas de Programação": ["vscode", "github", "terminal", "linux"],
        }
        self.tema = tema
        self.palavra = self.escolher_palavra()
        
    def escolher_palavra(self):
        # Escolhe uma palavra aleatória de acordo com o tema
        return random.choice(self.temas.get(self.tema, []))

    def get_palavra(self):
        return self.palavra
    
class LetrasCertas:
    def __init__(self, palavras):
        self.palavra = palavras  # Armazena a palavra secreta
        self.letras_acertadas = []  # Lista vazia para armazenar letras acertadas


    def tentar_letra(self, letra):  # método para entar adivinhar uma letra da palavra
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

