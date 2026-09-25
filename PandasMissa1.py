import pandas as pd
dados = {"nome": ["patrick", "marcio", "fabio", "thomas", "sergio"],
         "matricula": [1234567, 7654321, 9856730, 4356783, 4368794 ],
         "endereço": ["Rio de janeiro", "são paulo", "recife", "bahia", "minas gerais"]}

df = pd.DataFrame(dados)

print(df.head(3))
print(df.tail(3))


