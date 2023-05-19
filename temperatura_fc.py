def main():
    temperaturaF = float(input("Digite a temperatura em °F: "))
    temperaturaCelsius = converter_temperatura(temperaturaF)
    print(f"A temperatura em °Celsius é de: {temperaturaCelsius:.2f} graus")

def converter_temperatura(temperaturaF):
    temperaturaC = (5*temperaturaF - 160)/9
    return temperaturaC
main()