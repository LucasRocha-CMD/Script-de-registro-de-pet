from animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def set_raca(self, raca):
        self.raca = raca

    def get_raca(self):
        return self.raca

    def mostrar(self):
        return f'Gato: {self.nome}, Idade: {self.idade}, Raça: {self.raca}'
