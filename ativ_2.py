# Importações
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Entrada de dados
arquivo = "T:\Prof. Hugo\dados_seguros.csv"
dados_originais = pd.read_csv(arquivo, header=1)
dados = dados_originais.to_dict('list')


# dados = {"ramo" : ["Automóvel", "Saúde", "Incêndio", "Vida", "Riscos Diversos", "Habilitação", "Transporte", "Acidentes Pessoais", "Obrigatório Veículos", "Riscos de Engenharia", "Responsabilidade civil"], "%" : [33.6, 14.0, 12.9, 12.2, 5.5, 5.3, 3.1, 2.9, 1.7, 1.0, 0.9]}

percentuais = dados["%"]


# Cálculo dos quantis
Q1 = np.percentile(percentuais, 25, method="averaged_inverted_cdf")
Q2 = np.percentile(percentuais, 50, method="averaged_inverted_cdf")
Q3 = np.percentile(percentuais, 75, method="averaged_inverted_cdf")

DQ = Q3 - Q1 # cálculo da distância inter-quartil

# Cálculos dos limites
x1 = min(percentuais) # menor valor dos dados
xn = max(percentuais) # maior valor dos dados

li = max(x1, Q1 - 1.5 * DQ) # limite inferior
ls = min(xn, Q3 + 1.5 * DQ) # limite superior

boxplot1 = plt.boxplot(percentuais) # faz o boxplot dos dados


# Busca pelo Outlier
tamanho = len(percentuais) # determina o tamanho dos dados 
contador = range(tamanho) # cria um contador
outliers = [] # cria um vetor vazio de outliers

for i in contador:
    valor = percentuais[i] # pega o valor a ser testado 
    
    # testa se o valor atual é um outlier
    if valor > ls or valor < li:
        outliers.append(i) # anexa ao vetor se for um outlier
    
# Apresentação dos dados
print(f"Dados armazenados: {percentuais}")
print(f"Limite Superior = {ls} \nLimite Inferior = {li}")
print(f"A posição dos outliers são {outliers}")

# impressão dos outliers
tamanho_outliers = len(outliers)
contador_outliers = range(tamanho_outliers)
for i in contador_outliers:
    print("O outlier é:", dados["ramo"][i], "com valor:", dados["%"][i])
    
# plt.title("Boxplot dos Dados de Usinagem")
# plt.ylabel("Comprimento de Barras Usinadas")
plt.show() # apresenta o desenho do boxplot