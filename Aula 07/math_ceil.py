from os import system
import math

system("cls");

# Uma loja precisa armazenar seus produtos em caixas
# Cada caixa pode conter no máximo 10 produto

num_produtos = int(input("informe o número de produtos: "));
produtos_caixa = int(input("Informe a quantidade de produtos por caixa: "));

qtde_caixas = math.ceil(num_produtos/produtos_caixa);
print(f"Caixas necessárioas: {qtde_caixas}");