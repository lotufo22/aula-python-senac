from os import system
system("cls")

# Conversor de temperatura

temperatura = float(input('Temperatura a ser convertida: '));

print('Conversor de temperatura');
print('Qual unidade você deseja converter?');
print('1 - Celsius')
print('2 - Fahrenheit')
print('3 - Kelvin')
primeira = float(input('Digite a opção desejada: '));

print('Escolha a unidade para conversão: ');
print('1 - Fahrenheit');
print('2 - Kelvin');
print('3 - celsius');
segunda = int(input('Digite a opção desejada: '));


if(primeira == 1):
    if(segunda == 1):
        fahrenheit = (temperatura * 1.8) + 32;
        print(f'{temperatura}°C = {fahrenheit}°F');
    elif(segunda == 2):
        kelvin = temperatura + 273.15;
        print(f'{temperatura}°C = {kelvin}K');
    else:
        print('Opção inválida!');
elif(primeira == 2):
    if(segunda == 2):
        kelvin = 1.8 * (temperatura - 32) + 273.15;
        print(f'{temperatura}°F = {kelvin}K');
    elif(segunda == 3):
        celsius = (temperatura - 32) * 1.8;
        print(f'{temperatura}°F = {celsius}°C');
    else:
        print('Opção inválida!');
elif(primeira == 3):
    if(segunda == 2):
        fahrenheit = ((temperatura - 273.15) * 1.8) + 32;
        print(f'{temperatura}K = {fahrenheit}°F');
    elif(segunda == 3):
        celsius = temperatura - 273.15;
        print(f'{temperatura}K = {celsius}°C');
    else:
        print('Opção inválida!');