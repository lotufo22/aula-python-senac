from os import system
system("cls");


# Converter moedas REAL / DÓLAR / EURO (€ - \u20AC)

real = float(input("Digite o valor em Reais (R$): "));

print('Escolha a moeda para conversão: ')
print('1 - Dólar (US$)');
print('2 - Euro (€)');
print('3 - Peso Colombiano (COP)');

opcao = int(input("Opção: "));

if(opcao == 1):
    dolar = real / 5.13;
    print('R$ {:.2f} equivale a US$ {:.2f}' . format(real, dolar));
elif(opcao == 2):
    euro = real / 5.93;
    print('R$ {:.2f} equivale a \u20AC {:.2f}' . format(real, euro));
elif(opcao == 3):
    peso = real / 0.0016;
    print('R$ {:.2f} equivale a COP {:.2f}' . format(real, peso));
else:
    print('Opção inválida!');