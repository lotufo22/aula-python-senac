from datetime import datetime;
from os import system;
system("cls");

# Pegar data atual
data_atual = datetime.now();
print(f"Data atual: {data_atual}");
print(type(data_atual));

# Criar data (Ano, Mês, Dia, Hora, Minuto, Segundo, Microsegundo)
data_criada = datetime(2024, 9, 14, 10, 28, 11, 123456);
print(f"Data criada: {data_criada}");
print(type(data_criada))

# Pedir data ao usuário
data_usuario = input("Digite uma data no formato dd/mm/aaaa: ");
print(f"Data do usuario: {data_usuario}");
print(type(data_usuario));

# Converter string para data
data_convertida = datetime.strptime(data_usuario, '%d/%m/%Y');
print(f"Data convertida: {data_convertida}");
print(type(data_convertida));