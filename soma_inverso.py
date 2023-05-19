#Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.
#(Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).
def main():
    numero = int(input("Digite um número inteiro de 3 dígitos: "))
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = (numero % 100) % 101
    inverso = unidade * 100 + dezena * 10 + centena
    soma = numero + inverso
    print(f"A soma do numero com seu inverso é de {soma}")







main()