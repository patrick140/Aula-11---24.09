import pandas as pd
dados = {"nome": ["patrick", "marcio", "fabio", "thomas", "sergio"],
         "matricula": [1234567, 7654321, 9856730, 4356783, 4368794 ],
         "endereço": ["Rio de janeiro", "são paulo", "recife", "bahia", "minas gerais"]}

lista = [["salario", 145],["idade", 30]]

df = pd.DataFrame(lista, columns=["salario", "idade"])

df = pd.DataFrame( #designando nomes para as linhas
    {'idade': [25, 30, 35], 'cidade': ['SP', 'RJ', 'MG']},
    index=pd.Index(['Ana', 'Bruno', 'Carla'], name='nome')
)
#print(df)
print(df.loc["Ana"])


