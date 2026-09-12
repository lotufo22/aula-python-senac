import inss;
import irpf;
from os import system;
system("cls");

print("CLT - 1");
print("Contribuinte - 2");
registro = int(input("Escolha o seu registro: "));
salario = (float(input('Salário: ').replace(',', '.')));
dependente = int(input('Dependentes: '));

taxaInss = inss.taxa_inss(salario, registro);
aliquotaInss = inss.aliquota(salario);
deducaoInss = inss.deducao(salario);

taxaIrpf = irpf.taxa_irpf(salario, taxaInss, dependente);
aliquotaIrpf = irpf.aliquota(salario, taxaInss);
deducaoIrpf = irpf.deducao(salario, taxaInss);

salarioInss = salario - taxaInss;
salarioLiquido = salario - taxaInss - taxaIrpf;

print("\n");

print(f"Salário bruto: R${salario:.2f}\n".replace(".", ","));
print(f"Salário base IRPF: R${salarioInss:.2f}".replace(".", ","));

print(f"INSS: R${taxaInss:.2f}".replace(".", ","));
print(f"Aliquota: {aliquotaInss}%");
print(f"Dedução: R${deducaoInss:.2f}\n".replace(".", ","));

print(f"IRPF: R${taxaIrpf:.2f}".replace(".", ","));
print(f"Aliquota: {aliquotaIrpf}%");
print(f"Dedução: R${deducaoIrpf}\n".replace(".", ","));

print(f"Salário Líquido: R${salarioLiquido:.2f}".replace(".", ","));

# 3500 = liquido 3106.86