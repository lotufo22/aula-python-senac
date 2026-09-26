from os import system;
system("cls");

numeros = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove");
dez = ("dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove");
dezenas = ("", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa");

numero = int(input("Informe um número de 0 a 99: "));

while numero > 99: numero = int(input("Número inválido! Digite novamente: "));

if numero < 10:
    print(numeros[numero]);
elif numero < 20:
    print(dez[numero - 10]);
else:
    dezena = int(numero / 10);
    numeral = int(numero % 10);
    if numeral == 0:
        print(f"{str(dezenas[dezena]).capitalize()}");
    else:
        print(f"{str(dezenas[dezena]).capitalize()} e {numeros[numeral]}");