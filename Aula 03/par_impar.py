from os import system;
system("cls");

numero = int(input("Digite um número: "));

# Porcentagem em cáculo faz a divisão do número por 2 e retorna o resto da divisão.
resto = numero % 2;

if resto == 0:
    print('O número {} é PAR!' . format(numero));
else:
    print('O número {} é ÍMPAR!' . format(numero));
