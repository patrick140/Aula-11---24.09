import math

math.ceil(4.2)    # 5  (arredonda para cima)
math.floor(4.8)   # 4  (arredonda para baixo)
math.trunc(4.9)   # 4  (remove a parte decimal)
math.fabs(-7)     # 7.0 (valor absoluto como float)
math.sqrt(16)     # 4.0  (raiz quadrada)
math.pow(2, 10)   # 1024.0 (potência), pow(expoente, base)
math.gcd(12, 18)      # 6  (máximo divisor comum)
math.pi      # 3.141592653589793 valor de PI

numero = float(input("Digite um número: "))

print("A raiz quadrada é:", math.sqrt(numero))
print("O número elevado ao cubo é:", math.pow(numero, 3))
