#Exercício 1
# Objetivo do código Ajustar um polinômio de grau 4 aos dados fornecidos (pontos x e y), 
# e depois usar esse polinômio para estimar o valor de y para um x = 3.7.
import sympy as sy
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
x=[ 86.0, 93.3, 98.9, 104.4, 110.0]
y=[1552, 1548, 1544, 1538, 1532]
x = np.array(x)
y = np.array(y)
# Se x tem n valores, o valor que passaremos para o 3 parâmetro é n-1.
z = np.polyfit(x, y, 4)
print(z)
p = np.poly1d(z)
p(3.7)


#Exercicio 2
import sympy as sy
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
x=[ 86.0, 93.3, 98.9, 104.4, 110.0]
y=[1552, 1548, 1544, 1538, 1532]
x = np.array(x)
y = np.array(y)
z = np.polyfit(x, y, 4)
print(z)
p = np.poly1d(z)
p(105)

#Exercício 3
# utilizando o método de mínimos quadrados para encontrar o polinômio que melhor aproxima os valores de 
import sympy as sy
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
x=[ 86.0, 93.3, 98.9, 104.4, 110.0]
y=[1552, 1548, 1544, 1538, 1532]
x = np.array(x)
y = np.array(y)
z = np.polyfit(x, y, 4)
print(z)
p = np.poly1d(z)
p(95)

#Execicio - 3 com interp
# O código que você forneceu utiliza a função np.interp() do NumPy para realizar uma interpolação 
# linear entre os pontos fornecidos em x e y.
import numpy as np
x=[ 86.0, 93.3, 98.9, 104.4, 110.0]
y=[1552, 1548, 1544, 1538, 1532]
print(np.interp(95, x, y))

#exercicio 4
# O código que você forneceu realiza o ajuste de um polinômio de grau 4 aos dados fornecidos, e depois calcula as raízes do polinômio 
x=[ 86.0, 93.3, 98.9, 104.4, 110.0]
y=[1552, 1548, 1544, 1538, 1532]
x = np.array(x)
y = np.array(y)
z = np.polyfit(x, y, 4)
print(z)
p = np.poly1d(z)
np.roots(p-1539)