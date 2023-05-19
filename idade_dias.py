def main():
    print('Digite a idade em anos, meses e dias na ordem solicitada.')
    anos = int(input('Anos: '))
    meses = int(input('Meses: '))
    dias = int(input('Dias: '))
    print(f'A sua idade é {dias_total} dias.')
  
    dias_total = calcular_dias_totais(anos,meses,dias)

    def calcular_dias_totais(anos,meses,dias):
        dias_total = 365*anos + 30*meses + dias
        return dias_total
    

  
    

main()