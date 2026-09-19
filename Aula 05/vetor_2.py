from os import system;
system("cls");

total = int(input("Quantidade de nomes: "));

# vetor com parênteses '()' se torna um array imutável com tamanho fixo.
# lista com colchetes '[]' se torna uma list mutável com possibilidade de inserção;
nomes = [];

for i in range(total):
    system("cls");
    nome = str(input("Digite um nome: "));
    nomes.append(nome);

system("cls");

print("Lista de nomes:")
for i in range(total):
    print(f"{i} - {nomes[i]}");