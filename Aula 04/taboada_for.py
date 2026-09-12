import time;
from os import system;
system("cls");

numero = int(input("Digite um número: "));

# for de 0 a 11
for i in range(11):
    print(f"{i} x {numero} = {(i) * numero}");
    time.sleep(1);

print("");

# for de 1 a 11
for i in range(1, 11):
    print(f"{i} x {numero} = {(i) * numero}");
    time.sleep(1);