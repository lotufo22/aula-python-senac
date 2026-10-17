import random
from datetime import datetime
from os import system

system("cls");

class Personagem:
    def __init__(self, nome, energia, dano):
        self.nome = nome;
        self.energia = energia;
        self.dano = dano;

    def atacar(self, inimigo):
        energia = inimigo.energia;
        inimigo.energia -= self.dano;
        # Evita energia negativa
        inimigo.energia = max(inimigo.energia, 0);
        print(f'{self.nome} atacou {inimigo.nome} causando {self.dano} de dano!');
        print(f'{inimigo.nome} tinha {energia} e agora tem {inimigo.energia} de energia restante\n')

        if(inimigo.energia == 0):
            print(f'{inimigo.nome} foi derrotado por {self.nome}\n');

print('=' * 50);
print('Bem vindo ao jogo de batalha!');

mago = Personagem('Mago', 100, 20);
guerreiro = Personagem('Guerreiro', 120, 15);
arqueiro = Personagem("Arqueiro", random.randint(80, 150), random.randint(10, 25));

personagens = [mago, guerreiro, arqueiro];

while sum(1 for p in personagens if p.energia > 0) > 1:
    vivos = [p for p in personagens if p.energia > 0];
    atacar = random.choice(vivos);

    possiveis_alvos = [p for p in vivos if p != atacar];
    atacado = random.choice(possiveis_alvos);

vencedores = [p for p in personagens if p.energia > 0];
if(vencedores):
    vencedor = vencedores[0];
    print(f"Vencedor: {vencedor.nome}");
    print(f"Energia restante: {vencedor.nome}");
else:
    print("Todos os personagens foram derrotados")