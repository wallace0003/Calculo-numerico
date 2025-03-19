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
a1=(n*Sxy-Sx*Sy)/(n*Sxx-Sx**2)   #Calcula o coeficiente a1 da reta
a0=(Sxx*Sy-Sxy*Sx)/(n*Sxx-Sx**2) #Calcula o coeficiente a0 da reta
print(a1)
print(a0)


#Execício 2
def funcao_reta(x):
    reta = -7.40*x + 171.87
    return reta
print(funcao_reta(100))


#Exercício 3
def Residuo(x,y,b0,b1):
    n = len(y)
    RS = 0
    for i in range(0,n):
         y_pred=b0+b1*x[i]
         RS = RS + (y[i]-y_pred)**2
    return RS
print('RS:', Residuo(x,y,a0,a1))


#Exercício 4
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
x = x.reshape(-1, 1)
modelo = LinearRegression().fit(x, y)
R2 = r2_score(y, modelo.predict(x))
print('R2:', R2)