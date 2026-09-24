import pandas as pd #importar a biblioteca pandas que sera chamada pelo apelido "pd"

dados = { #dicionario que sera transformado em um dataframe
'cargos': ["assistente", "auxiliar", "gerente"],
'salários': [2500, 1800, 7500] 
 }

dados_bi = pd.DataFrame(dados) # .DataFrame é o comando para criar o dataframe(a partir de algum dado)

print(dados_bi)
