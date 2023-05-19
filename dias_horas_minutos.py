
def main():
    minutos = int(input("Digite o valor em minutos:"))
    dias = calcular_dias(minutos)
    horas = calcular_horas(minutos,dias)
    minutosrestantes = calcular_minutos(minutos,dias,horas)
    print(f"{dias} dias, {horas} horas e {minutosrestantes} minutos") 

def calcular_dias(minutos):
    dias = minutos//1440
    return dias

def calcular_horas(minutos,dias):
    horas = (minutos - dias*1440)//60
    return horas

def calcular_minutos(minutos,dias,horas):
    minutosrestantes = minutos - dias*1440 - horas*60
    return minutosrestantes
    



main()