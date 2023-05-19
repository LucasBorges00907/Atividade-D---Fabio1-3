def main():
    x1 = int(input('Digite o "x" do primeiro ponto: '))
    y1 = int(input('Digite o "y" do primeiro ponto: '))
    x2 = int(input('Digite o "x" do segundo ponto: '))
    y2 = int(input('Digite o "y" do segundo ponto: '))
   
    distancia = calcular_distancia(x1,y1,x2,y2)

    print(f'A distância entre ({x1},{y1}) e ({x2},{y2}) é {distancia:.2f}.')

def calcular_distancia(x1,y1,x2,y2):
    distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** (1/2)
    return distancia





main()