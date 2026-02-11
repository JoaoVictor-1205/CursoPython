from dataclasses import dataclass, asdict, astuple, field

@dataclass
class Pessoa:
    nome: str = field(
        default='Not Sent',
        repr=False,
    )
    sobrenome: str = 'Not Sent'
    idade : int = 0
    endereco: list[str] = field(default_factory=list)


if __name__ == '__main__':
    p1 = Pessoa('João', 'Silva')
    print(p1)
    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1))