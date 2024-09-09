import json

def calcular_soma(indice):
    soma = 0
    k = 0
    while k < indice:
        k += 1
        soma += k
    return soma

def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

def analise_faturamento(faturamento_json):
    data = json.loads(faturamento_json)
    valores = [item["valor"] for item in data["faturamento"] if item["valor"] > 0]
    menor_valor = min(valores)
    maior_valor = max(valores)
    media_mensal = sum(valores) / len(valores)
    dias_acima_da_media = len([valor for valor in valores if valor > media_mensal])
    return menor_valor, maior_valor, dias_acima_da_media

def percentual_representacao(faturamento):
    total_faturamento = sum(faturamento.values())
    percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}
    return percentuais


def inverter_string(s):
    return s[::-1]


indice = 13
soma = calcular_soma(indice)
print(f"SOMA dos primeiros {indice} números: {soma}")

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")

faturamento_json = '''
{
    "faturamento": [
        {"dia": 1, "valor": 1500},
        {"dia": 2, "valor": 2300},
        {"dia": 3, "valor": 0},
        {"dia": 4, "valor": 1800},
        {"dia": 5, "valor": 1700},
        {"dia": 6, "valor": 1600},
        {"dia": 7, "valor": 2200}
    ]
}
'''
menor_valor, maior_valor, dias_acima_da_media = analise_faturamento(faturamento_json)
print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
percentuais = percentual_representacao(faturamento_estados)
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

string = input("Digite uma string para inverter: ")
print(f"String invertida: {inverter_string(string)}")
