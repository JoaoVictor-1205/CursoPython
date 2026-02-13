from collections import namedtuple
from typing import NamedTuple

class Carta(NamedTuple):
    naipe: str
    valor: str

Carta2 = namedtuple(
    'Carta', ['naipe', 'valor'],
    defaults=['NAIPE', 'VALOR']
    )
as_espada = Carta('Espada', 'Ás')


for valor in as_espada:
    print(valor)