def taxa_inss(salario, registro):
    if(salario <= 1621.00): return salario * 0.075;
    elif(salario <= 2902.84): return (salario * 0.09) - 24.32;
    elif(salario <= 4354.27): return (salario * 0.12) - 111.40;
    elif(salario <= 8475.55): return (salario * 0.14) - 198.49;
    else:

        # match registro:
        #     case 1: inss = salario - 988.07;
        #     case _: inss = 932.31;

        if (registro == 1): return 988.07;
        else: return 932.31;

def aliquota(salario):
    if(salario <= 1621.00): return 7.5;
    elif(salario <= 2902.84): return 9;
    elif(salario <= 4354.27): return 12;
    elif(salario <= 8475.55): return 14;
    else: return 0;

def deducao(salario):
    if(salario <= 1621.00): return 0;
    elif(salario <= 2902.84): return 24.32;
    elif(salario <= 4354.27): return 111.41;
    elif(salario <= 8475.55): return 198.50;
    else: return 0;