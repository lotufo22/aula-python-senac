from os import system
system("cls");

def somar(a, b):
    try:
        print(f"Somar {a} + {b} = {a + b}");
    except:
        print("Erro desconhecido");

def subtrair(a, b):
    try:
        print(f"Subtrair {a} - {b} = {a - b}");
    except:
        print("Erro desconhecido");

def multiplicar(a, b):
    try:
        print(f"Multiplicar {a} x {b} = {a * b}");
    except:
        print("Erro desconhecido");

def dividir(a, b):
    try:
        print(f"Dividir {a} / {b} = {a / b}");
    except ZeroDivisionError as erro:
        print(f"Impossível divisão por zero. Mensagem de Erro: {erro}");
    except:
        print("Erro desconhecido");

opcao = "";

while opcao != "N":
    system("cls");

    num1 = float(input("Informe o primeiro número: "));
    num2 = float(input("Informe o segundo número: "));

    opcao = int(input('''
Opções:
[1] - Somar
[2] - Subtrair
[3] - Multiplicar
[4] - Dividir
Escolha uma opção acima: 
'''));
    system("cls");
    
    if opcao < 1 and opcao > 4: print("Opção inválida!")

    if opcao == 1:
        somar(num1, num2);
    elif opcao == 2:
        subtrair(num1, num2);
    elif opcao == 3:
        multiplicar(num1, num2);
    elif opcao == 4:
        dividir(num1, num2);
    else:
        print("Opção inválida!");

    opcao = input("Digite N para terminar ou Enter para outra operação: ").upper();