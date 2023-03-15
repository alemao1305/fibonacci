import json

# Lendo o arquivo JSON com os dados de faturamento diário
with open('faturamento.json', 'r') as f:
    faturamento_diario = json.load(f)

# Calculando o menor e o maior valor de faturamento diário
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

# Calculando a média de faturamento diário
media_mensal = sum(faturamento_diario) / len(faturamento_diario)

# Calculando o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for f in faturamento_diario if f > media_mensal)

# Exibindo os resultados
print("Menor valor de faturamento diário:", menor_valor)
print("Maior valor de faturamento diário:", maior_valor)
print("Número de dias com faturamento acima da média mensal:", dias_acima_da_media)

