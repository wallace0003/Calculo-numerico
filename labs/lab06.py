#Exercício 1
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets
df = pd.read_csv('water_potability.csv', header=(0))
print("Número de linhas e colunas:",df.shape)
df.head(25)
df = df.dropna()
print("Número de linhas e colunas:",df.shape)
df.head(25)

#Exercício 2
import seaborn as sns
corr = df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='Purples')

#Exercício 3
import seaborn as sns
import statsmodels.formula.api as sm
model = sm.ols(formula='ph ~ Hardness', data=df)
result = model.fit()
print(result.summary())

#exercicio 4
model = sm.ols(formula="ph ~ Hardness+Solids+Chloramines", data=df)
result = model.fit()
print(result.summary())