#Classe despesa
class Despesa:
    def __init__(self, id, valor, descricao, data, categoria):
        self.id = id
        self.valor = valor
        self.descricao = descricao
        self.data = data
        self.categoria = categoria
    def __str__(self):
        return f"{self.id} | {self.valor:.2f} | {self.descricao} | {self.data} | {self.categoria}" 