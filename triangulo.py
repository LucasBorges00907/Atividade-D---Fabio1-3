def main():

    base = float(input('Digite a medida da base do triângulo: '))
    altura = float(input('Digite a medida da altura do triângulo: '))

    area = calcular_area(base,altura)

    print (f'A área do triângulo é de: {area}')

def calcular_area(base,altura):
    area = (base*altura)/2
    return area

main()


