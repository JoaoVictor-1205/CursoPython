from dataclasses import dataclass
from collections.abc import Sequence
from typing import Iterator

@dataclass
class MyList(Sequence):
    def __init__(self, *args):
        self._data = {}
        self._index = 0

    def append(self, valor):
        self._data[self._index] = valor
        self._index += 1

    def __iter__(self):
        ...

    def __len__(self) -> int:
        return self._index
    
    def __getitem__(self, index):
        return self._data[index]

lista = MyList()
lista.append('Carro')
lista.append('Vassoura')
print(lista.__getitem__(0))