import random
import time

class Criatura:
    nome: str
    vida: int
    defesa: int

    def __init__(self, nome: str, vida: int, defesa: int) -> None:
        self.nome = nome
        self.vida = vida
        self.defesa = defesa

    # O método não retorna nada, por isso usamos -> None
    def atacar(self, oponente: "Criatura") -> None:
        ataque = random.randint(5, 15)
        if ataque < self.defesa:
            dano = 0
            oponente.vida -=  dano
        else:
            dano = ataque - self.defesa
            oponente.vida -=  dano

        print(f"{self.nome} usou um ataque {ataque}!")
        print(f"Causou {dano} de dano em {oponente.nome}!")

        if oponente.vida < 0:
            oponente.vida = 0



cria1: Criatura = Criatura("Esqueleto", 50, 2)
cria2: Criatura = Criatura("Zombie", 60, 3)

print(" A BATALHA VAI COMEÇAR!\n")
print(f"{cria1.nome} (vida: {cria1.vida}) VS {cria2.nome} (vida: {cria2.vida})\n")
print("-" * 40)


turno: int = 1
while cria1.vida > 0 and cria2.vida > 0:
    print(f"\n RODADA {turno}")

    cria1.atacar(cria2)
    print(f"vida de {cria2.nome}: {cria2.vida}")

    if cria2.vida <= 0:
        break

    print("-" * 20)
    time.sleep(1)

    cria2.atacar(cria1)
    print(f"vida de {cria1.nome}: {cria1.vida}")

    turno += 1
    print("-" * 40)
    time.sleep(1)


print("Fim da batalha! ")
if cria1.vida > 0:
    print(f"{cria1.nome} é o vencedor!")
else:
    print(f"{cria2.nome} é o vencedor!")