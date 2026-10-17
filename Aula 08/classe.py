from datetime import datetime
from os import system
system("cls");
import time;

class Servico:
    # Contrutor / Initialize da Classe
    def __init__(self, descricao, preco):
        self.descricao = descricao;
        self.preco = preco;
        self.data = datetime.today().strftime('%d/%m/%Y');
        self.horario = datetime.now().strftime('%H:%M:%S');

    # Método para exibir os dados do serviço
    def exibir_dados(self):
        print(f'Data: {self.data}');
        print(f'Horário: {self.horario}');
        print(f'Descricao: {self.descricao}');
        print(f'Preço: R${self.preco:.2f}');

    # Método para salvar dados em TXT
    def salvar_historico(self):
        # a letra que determina se o ponteiro no arquivo irá para o final, começo, sobreescrever, incrementar, etc
        # Abre o arquivo em modo de escrita (append) para adicionar novos registros
        # utf-8 é usado para suportar caracteres especiais
        with open('historico_servicos.txt', 'a', encoding='utf-8') as f: 
            f.write(f'Data: {self.data}\n')
            f.write(f'Horário: {self.horario}\n')
            f.write(f'Descrição: {self.descricao}\n');
            f.write(f'Preço: R${self.preco:.2f}\n');
            f.write('-' * 40 + '\n');



# Iniciando o código principal
continuar = 'S';

while(continuar.upper() != 'X'):
    system("cls");

    print(' == CADASTRO DE SERVIÇOS == ');


    descricao = input("Informe a descrição do serviço: ");
    preco = input("Informa o preço do serviço: ");

    try:
        preco = float(preco);
    except:
        print('Valor inválido. O preço deve ser um número.');
        time.sleep(3);
        continue;

    system("cls");

    # Criando uma instância (criar registro ou informação da classe) da classe serviço
    servico = Servico(descricao, preco);
    # Exibindo dados
    servico.exibir_dados();
    print('-' * 40);

    try:
        servico.salvar_historico();
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}");

    continuar = input('Tecle "Enter" para continuar ou "X" para sair: ');