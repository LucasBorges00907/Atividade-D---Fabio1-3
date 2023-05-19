#Leia um valor em m, calcule e escreva o equivalente em cm.
def main():
    metros = float(input("Digite o valor em metros:"))
    cm = calcular_valor_cm(metros)
    print(f"O valor em cm é: {cm}")

def calcular_valor_cm(metros):
    cm = metros*100
    return cm





main()