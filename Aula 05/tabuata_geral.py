import time;
from os import system;
system("cls");

# Inicia a contagem do multiplicador
for i in range(1, 11):
    print(f"Tabuada do {i}\n");
    # Inicia a contagem do multiplicador
    for j in range(11):
        print(f"{i} x {j} = {j*i}");
        time.sleep(0.5);

    print("");