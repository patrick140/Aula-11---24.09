def somar_numeros(num1, num2):
    soma = num1 + num2
    return soma
try:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o Segundo numero: "))
except(ValueError):
    print("ERRO! Valor invalido digitado.")
else:
    print(f"A soma dos dois numeros é {somar_numeros(numero1, numero2)}.")
finally:
    print("Fim do programa.")

