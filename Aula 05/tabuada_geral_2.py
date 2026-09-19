import time;
from os import system;
system("cls");

# Inicia a contagem do multiplicador
for i in range(1, 11):
    # Limpa a variável "linha"
    linha = "";
    for j in range(1,11):
        # Armazena toda a tabuada
        # ': >4' = Totaliza 04 caracteres, completando com espaço vazio a esquerda
        # ': <4' = Totaliza 04 caracteres, completando com espaço vazio a direita
        linha += f'{i*j: <4}';
    
    # Mostra os resultados do "multiplicando"
    print(linha);
    time.sleep(0.5);