def main():
    salario = float(input('Digite o seu salário atual: R$ '))
    novo_salario =  calcular_novo_salario(salario)
    print(f'O seu novo salário é R$ {novo_salario:.2f}.')
    
def calcular_novo_salario(salario):
    novo_salario= salario*1.25
    return novo_salario

main()

