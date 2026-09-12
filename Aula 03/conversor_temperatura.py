from os import system
system("cls")

# Conversor de temperatura

temperatura = float(input('Temperatura a ser convertida: '));

print('Escolha a unidade para conversão: ');
print('1 - Fahrenheit');
print('2 - Kelvin');
opcao = int(input('Digite a opção desejada: '));


if(opcao == 1):
    fahrenheit = (temperatura * 1.8) + 32;
    print(f'{temperatura}°C = {fahrenheit}°F');
elif(opcao == 2):
    kelvin = temperatura + 273.15;
    print(f'{temperatura}°C = {kelvin}K');
else:
    print('Opção inválida!');