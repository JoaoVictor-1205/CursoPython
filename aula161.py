from dataclasses import dataclass, asdict

@dataclass
class MyList:
    def __init__(self, *args):
        self._data = {}
        self.index = 0

    def append(self, valor):
        self._data[self.index] = valor
        self.index += 1

lista = MyList()
lista.append('Carro')
print(lista._data)