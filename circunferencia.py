def main():
 raio = float(input("Digite o valor do raio(cm): "))
 comprimento = calcular_comprimento(raio)
 print(f"O Comprimento da circnuferêncie é: {comprimento:.2f}cm")
 
def calcular_comprimento(raio):
 comprimento = 2*3.14*raio
 return comprimento

main()