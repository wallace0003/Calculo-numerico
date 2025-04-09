#lab de regressão linear

#Exercício 1
import numpy as np
import matplotlib.pyplot as plt
# x : 1,8 ; 2,7 ; 4,0 ; 7,0 ; 14,0 ; 26,0

# y : 250 ; 163 ; 103 ; 60 ; 29; 15

# define os dados
x = np.array([1.8, 2.7 ,4.0,7.0, 14.0, 26.0]) 
y = np.array([250, 163, 103, 60, 29, 15])
n = np.size(x) 
Sx= np.sum(x)
Sy=np.sum(y)
Sxy=np.sum(x*y)
Sxx=np.sum(x*x)   
a1=(n*Sxy-Sx*Sy)/(n*Sxx-Sx**2)   #Calcula o coeficiente a1 da reta -> coeficiente angular da reta.
a0=(Sxx*Sy-Sxy*Sx)/(n*Sxx-Sx**2) #Calcula o coeficiente a0 da reta -> coeficiente linear da reta.
print(a1)
print(a0)


#Retornar o valor da reta para um determinado valor de x
#Execício 2 
def funcao_reta(x):
    reta = -7.40*x + 171.87
    return reta
print(funcao_reta(100))


# Ela calcula o erro total da regressão linear, ou seja, quão longe a reta estimada está dos dados reais.
#Exercício 3
def Residuo(x,y,b0,b1):
    n = len(y) #número de pontos
    RS = 0   #inicializa o somatório do erro
    for i in range(0,n):
         y_pred=b0+b1*x[i] # valor predito pela reta
         RS = RS + (y[i]-y_pred)**2 # erro quadrado acumulado
    return RS
print('RS:', Residuo(x,y,a0,a1))


# Exercício 4
# Essa função calcula a matriz de correlação de Pearson, que mede a força e a direção da relação linear entre duas variáveis.
# A saída será uma matriz 2×2:
# Onde r é o coeficiente de correlação de Pearson entre x e y.
# r ≈ 1 → Correlação linear positiva forte
# r ≈ -1 → Correlação linear negativa forte
# r ≈ 0 → Sem correlação linear
import numpy as np
x = np.array([1.8, 2.7 ,4.0,7.0, 14.0, 26.0]) 
y = np.array([250, 163, 103, 60, 29, 15])
correlacao = np.corrcoef(x, y)
print(correlacao)


# Exercício 5
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
x = np.array([1.8, 2.7 ,4.0,7.0, 14.0, 26.0]) 
y = np.array([250, 163, 103, 60, 29, 15])
x = np.array(x)
# x é convertido para uma matriz coluna com .reshape(-1, 1) porque o sklearn exige que as 
# variáveis preditoras (x) tenham formato de matriz 2D.
x = x.reshape(-1, 1)
#Aqui, o modelo aprende os coeficientes a₀ (intercepto) e a₁ (inclinação) da reta que melhor se ajusta aos dados.
modelo = LinearRegression().fit(x, y)
R2 = r2_score(y, modelo.predict(x))
# O que é o R2? -> É o coeficiente de determinação, que mede o quanto da variabilidade de y é explicada pelo modelo.
# R² = 1 → o modelo explica 100% da variação em y
# R² = 0 → o modelo não explica nada
# R² < 0 → o modelo é pior que uma média constante
print('R2:', R2)
# O print('R2:', R2) vai te mostrar quão bom está o ajuste da reta aos seus dados.