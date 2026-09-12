from os import system
system('cls');
# system('color 0a');

# Funções para trabalhar com textos

nomeCompleto = input('Digite o seu nome completo: ');

# len = lenght - Conta o número de caracteres de uma string
# 'variavel'.replace("a", "b") - Substitui o caractere "a pelo caractere "b" na string

# strip() - remove espaços em branco antes e depois do texto
# upper() - texto maiúsculo
# lower() - texto minúsculo
# captalize() - primeira letra maiúscula
# title() - primeira letra de cada palavra maiúscula

print('- Função para contar caracteres: ', len(nomeCompleto));
print(f'Olá, {nomeCompleto}! O seu nome tem {len(nomeCompleto.replace(" ", "").strip())} caracteres.');
print('- Função para texto maiúsculo: ', nomeCompleto.upper());
print('- Função para texto minúsculo: ', nomeCompleto.lower());
print('- Função para primeira letra maiúscula: ', nomeCompleto.capitalize());
print('- Função para primeira letra de cada palavra maiúscula: ', nomeCompleto.title());
print('- Função para remover espaços em branco antes e depois do texto: ', nomeCompleto.strip());

# Como pegar parte do texto

print('- Primeira letra: ', nomeCompleto[0]);
print('- Primeira palavra: ', nomeCompleto[0:6]);

# find - Retorna a posição do caractere ou palavra na string
espaco = nomeCompleto.find(' ');
print('- Primeira palavra: ', nomeCompleto[0:espaco]);

# replace - Substitui um caratere por outro na string
print('- Remover espaços vazios: ', nomeCompleto.replace(' ', ''));
print('- Conta letras sem espaços: ', len(nomeCompleto.replace(' ', '')));

primeiroNome = nomeCompleto[0:espaco];
novoNome = input("Digite o seu novo nome: ");

print('- Substituindo o primeiro nome pelo novo nome: ', nomeCompleto.replace(primeiroNome, novoNome));