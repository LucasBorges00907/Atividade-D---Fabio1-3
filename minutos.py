def main():
    
    minutos_entrada = int(input('Digite um valor em minutos: '))
    
    horas = calcular_horas(minutos_entrada)
    minutos_saida = calcular_minutos(minutos_entrada)
    
    print(f'O resultado é {horas} horas e {minutos_saida} minutos')


def calcular_horas(minutos_entrada):
    horas = minutos_entrada // 60
    return horas

def calcular_minutos(minutos_entrada):
    minutos_saida = minutos_entrada % 60
    return minutos_saida


main()