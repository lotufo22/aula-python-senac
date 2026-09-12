valor_dependente = 189.59;

def taxa_irpf(salario, inss, dependentes):
    total_dependentes = valor_dependentes(dependentes);
    salarioInss = salario_base(salario, inss) - total_dependentes;

    if(salarioInss <= 2428.80):
        aliquota = 0;
        parcela = 0;
    elif(salarioInss <= 2826.65):
        aliquota = 0.075;
        parcela = 182.16;
    elif(salarioInss <= 3751.05):
        aliquota = 0.15;
        parcela = 394.16;
    elif(salarioInss <= 4664.68):
        aliquota = 0.225;
        parcela = 675.49;
    else: 
        aliquota = 0.275;
        parcela = 908.73;

    taxa_irpf = (salarioInss * aliquota) - parcela;

    return taxa_irpf;

def aliquota(salario, inss):
    salarioInss = salario_base(salario, inss);

    if(salarioInss <= 2428.80): return 0;
    elif(salarioInss <= 2826.65): return 7.5;
    elif(salarioInss <= 3751.05): return 15;
    elif(salarioInss <= 4664.68): return 22.5;
    else: return 27.5;

def deducao(salario, inss):
    salarioInss = salario_base(salario, inss);

    if(salarioInss <= 2428.80): return 0;
    elif(salarioInss <= 2826.65): return 182.16;
    elif(salarioInss <= 3751.05): return 394.16;
    elif(salarioInss <= 4664.68): return 675.49;
    else: return 908.73;

def salario_base(salario, inss):
    return salario - inss;

def valor_dependentes(dependente):
    return valor_dependente * dependente;