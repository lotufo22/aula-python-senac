from os import system
system("cls");

clientes = [];
telefones = [];

opcao = "";

while opcao != "X":
    system("cls");
    nome = input("Digite o nome do cliente: ");
    telefone = input("Digite o telefone do cliente: ");

    clientes.append(nome);
    telefones.append(telefone);

    system("cls");

    print("-- CADASTRO REALIZADO COM SUCESSO --");

    opcao = input(f"Aperte X para finalizar ou Enter para continuar: ").upper();

system("cls");

for i in range(len(clientes)):
    print(f"Nome: {clientes[i]} - Celular: {telefones[i]}");