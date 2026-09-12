from os import system
system("cls")

# Calculadora de IMC (Índice de Massa Corporal)

altura = input('Digite sua altura (m): ');
altura = float(altura.replace(",", "."));
peso = float(input("Digite seu peso (kg): ").replace(",", "."));

# ** - Exponenciação
# imc = peso / (altura * altura)
imc = peso / (altura ** 2);

# Formas de apresentar a variável
print('Seu IMC é {}' . format(imc));
print(f'Seu IMC é {imc}');
print('Seu IMC é {:.2f}' . format(imc));
print(f'Seu IMC é {imc:.2f}');

if(imc < 18.5):
    print(f'IMC: {imc:.2f} - Magreza');
elif(imc < 25):
    print(f'IMC: {imc:.2f} - Normal');
elif(imc < 30):
    print(f'IMC: {imc:.2f} - Obesidade Classe I');
elif(imc >= 30 and imc < 40):
    print(f'IMC: {imc:.2f} - Obesidade Classe II');
else:
    print(f'IMC: {imc:.2f} - Obesidade Classe III');