import time;
from os import system
system("cls");

numero = int(input("Informe um número maior que 0: "));
count = 0;

if(numero <= 0): print("Número inválido");
else:
    #  Laço for
    for i in range(numero):
        print(f"O valor da variável i: {i}");
        time.sleep(1);