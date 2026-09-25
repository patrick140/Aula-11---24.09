def somar_numeros(num1, num2):
    soma = num1 + num2
    return soma
try:
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
except ValueError:
    print("ERRO! valor invalido!")
else:
    print(f"A soma dos dois numeros são: {somar_numeros(numero1, numero2)}")

