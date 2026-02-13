from dataclasses import dataclass
from collections.abc import Sequence
from typing import Iterator

@dataclass
class MyList(Sequence):
    def __init__(self, *args):
        self._data = {}
        self._index = 0
        self.next_index = 0

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int:
        return self._index
    
    def __getitem__(self, index):
        return self._data[index]
    
    def __setitem__(self, index, valor):
        self._data[index] = valor;

    
    
    def __next__(self):
        if self.next_index >= self._index:
            self.next_index = 0
            raise StopIteration
        
        value = self._data[self.next_index]
        self.next_index += 1
        return value
    
    def __iter__(self) -> Iterator:
        return self

lista = MyList()
lista.append('Carro')
lista.append('Vassoura', 'Caderno')
lista[2] = 'mustang'

for item in lista:
    print(item)
for item in lista:
    print(item)
