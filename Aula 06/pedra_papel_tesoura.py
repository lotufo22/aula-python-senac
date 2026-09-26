from os import system
import random; # random = utilizar escolha aleatória
system("cls");

continua = "S";

while continua == "S":
    system("cls");

    computador = random.randint(0, 2);
    jogador = int(input('''Opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura
    Escolha uma opção: '''));

    system("cls");

    if jogador >= 0 and jogador <= 2:
        pecas = ("Pedra", "Papel", "Tesoura");
        print(f"\nComputador escolheu {pecas[computador]}");
        print(f"Você escolheu {pecas[jogador]}\n");

        tabela = ((0, 1, -1), (-1, 0, 1), (1, -1, 0));
        jogada = tabela[computador][jogador];

        if jogada == -1: print("Você perdeu!\n");
        elif jogada == 0: print("Empate\n");
        else: print("Você venceu a MÁQUINA!\n");
    else:
        print("Opção INVÁLIDA!\n");

    continua = (input("Digite [S] para jogar novamente: ")).upper();



'''             tabela

                 Jogador
                0   1  -1
computador     -1   0   1
                1   0  -1
'''