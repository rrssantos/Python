def desc_salario (salario, imposto=27.):
    return salario - (salario * imposto * 0.01)

def main():
    sal = float(input("Digite o Salario: "))
    x = desc_salario(sal, 10)
    print(x)
