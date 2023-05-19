#Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos
#segundos ele corresponde.
def main():
    segundos = int(input("Digite a quantidade de segundos: "))
    horas = calcular_horas(segundos)
    minutos = calcular_minutos(horas,segundos)
    segundos2 = calcular_segundos(segundos,horas,minutos)

    print(f"{horas}horas, {minutos} minutos e {segundos2} segundos ")

def calcular_segundos(segundos,horas,minutos):
    segundos2 = segundos -horas*3600-minutos*60
    return segundos2

def calcular_horas(segundos):
    horas = segundos//3600
    return horas

def calcular_minutos(horas,segundos):
    minutos = (segundos - (3600*horas))//60
    return minutos
    





main()