from os import system;
from datetime import datetime;
system("cls");

def calcular_idade(nascimento):
    # Data atual
    data_atual = datetime.today();
    data_nascimento = datetime.strptime(nascimento, '%d/%m/%Y');

    # Calcular idade
    idade = data_atual.year - data_nascimento.year;
    # Se a data atual for maior que a do nascimento retorna true que é 1, então se for menor irá subtrair 1 da idade
    aniversario_passou = ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day));

    return idade - aniversario_passou;


def idade_dias(data_nascimento):
    # Data atual
    data_atual = datetime.now();
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y');

    # Calcular idade em dias
    idade_dias = (data_atual - data_nascimento).days;
    return idade_dias;

# Pedir data nascimento do usuário
data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ");

print(f'Sua idade é: {calcular_idade(data_nascimento)} anos.');
print(f'Você já viveu: {idade_dias(data_nascimento)} dias.');