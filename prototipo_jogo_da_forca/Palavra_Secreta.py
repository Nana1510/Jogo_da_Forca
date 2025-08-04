import random

class PalavraSecreta:
    def __init__(self, tema):
        self.temas = {
            "Linguagens de Programação": ["python", "java", "javascript"],
            "Conceitos de Programação": ["variavel", "função", "classe", "objeto", "heranca", "polimorfismo"],
            "Ferramentas de Programação": ["vscode", "github", "terminal", "linux"],
        }
        self.tema = tema
        self.palavra = self.escolher_palavra()
        self.letras_acertadas = []  # Adicionado

    def escolher_palavra(self):
        return random.choice(self.temas.get(self.tema, []))

    def get_palavra(self):
        return self.palavra

    def tentar_letra(self, letra):
        letra = letra.lower()
        if letra in self.palavra and letra not in self.letras_acertadas:
            self.letras_acertadas.append(letra)
            return True
        return False