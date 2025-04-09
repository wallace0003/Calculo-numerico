
#Exercício 1
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets
df = pd.read_csv('water_potability.csv', header=(0))
print("Número de linhas e colunas:",df.shape)
df.head(25)
# dropna é usado para apagar as linhas que tem valores nulos.
df = df.dropna()
print("Número de linhas e colunas:",df.shape)
df.head(25)

#Exercício 2
# Isso é usado para entender a correlação entre as variáveis.
import seaborn as sns
corr = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='Purples')


#Exercício 3
import seaborn as sns
import statsmodels.formula.api as sm
# ph como variável dependente (resposta)
# Hardness como variável independente (explicativa)
# E os dados estão no DataFrame df
model = sm.ols(formula='ph ~ Hardness', data=df)
# Ajusta o modelo aos dados (isto é, encontra os melhores coeficientes para a equação da reta).
result = model.fit()
# Mostra um resumo estatístico completo do modelo, incluindo:
print(result.summary())

# exercicio 4
# Esse código agora está criando um modelo de regressão linear múltipla — ou seja, com mais de uma variável explicativa.
# Quero prever o valor de ph com base em Hardness, Solids e Chloramines.
# ph como variável dependente (y)
# Hardness Solids Chloramines como as variáveis independentes (x)
model = sm.ols(formula="ph ~ Hardness+Solids+Chloramines", data=df)
result = model.fit()
print(result.summary())
# OBS
# Se algum coeficiente tiver p-valor muito alto, pode significar que aquela variável não está contribuindo significativamente para o modelo.
# Um R² muito próximo de 1 indica bom ajuste, mas cuidado com overfitting (especialmente com muitos preditores).