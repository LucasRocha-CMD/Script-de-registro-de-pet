from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.porte = porte

    def set_porte(self, porte):
        self.porte = porte

    def get_porte(self):
        return self.porte

    def mostrar(self):
        return f'Cachorro: {self.nome}, Idade: {self.idade}, Porte: {self.porte}'
