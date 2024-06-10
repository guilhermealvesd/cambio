#Importando a biblioteca e as suas funcionalidades

from forex_python.converter import CurrencyRates

#Programa Principal

valor = str(input('Informe o valor da moeda a ser convertida: '))
valor = float(valor.replace(',', '.'))
moeda_origem = input('Informe a moeda de origem: ').upper()
moeda_destino = input('Informe a moeda de destino: ').upper()

#Faz a conversão de acordo com a taxa de câmbio do dia
result = CurrencyRates().convert(moeda_origem, moeda_destino, valor)

#Exibe o resultado

print(f'${valor:,.2f} {moeda_origem} = ${result:,.2f}{moeda_destino}')