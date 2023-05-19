def main():
    a = int(input('Digite o valor de A: '))
    b = int(input('Digite o valor de B: '))
    c = int(input('Digite o valor de C: '))
    print (f"O valor de D é {d}")

   
    r = calcular_r(a,b)
    s = calcular_s(b,c)
    d = calcular_d(r,s)

   
def calcular_r(a,b):
    r = (a + b) ** 2
    return r

def calcular_s(b,c):
    s = (b + c) ** 2
    return s

def calcular_d(r,s):
    d = (r + s) / 2
    return d






main()