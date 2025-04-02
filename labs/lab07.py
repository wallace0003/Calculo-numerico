#Exercício 1
import sympy as sy
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
x=[ 86.0, 93.3, 98.9, 104.4, 110.0]
y=[1552, 1548, 1544, 1538, 1532]
x = np.array(x)
y = np.array(y)
# valor 1 representa o grau do polinomio
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
# valor 1 representa o grau do polinomio
z = np.polyfit(x, y, 4)
print(z)
p = np.poly1d(z)
p(105)

#Exercício 3
import sympy as sy
import numpy as np
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
x=[ 86.0, 93.3, 98.9, 104.4, 110.0]
y=[1552, 1548, 1544, 1538, 1532]
x = np.array(x)
y = np.array(y)
# valor 1 representa o grau do polinomio
z = np.polyfit(x, y, 4)
print(z)
p = np.poly1d(z)
p(95)

#Execicio - 3 com interp
import numpy as np
x=[ 86.0, 93.3, 98.9, 104.4, 110.0]
y=[1552, 1548, 1544, 1538, 1532]
print(np.interp(95, x, y))

#exercicio 4
x=[ 86.0, 93.3, 98.9, 104.4, 110.0]
y=[1552, 1548, 1544, 1538, 1532]
x = np.array(x)
y = np.array(y)
z = np.polyfit(x, y, 4)
print(z)
p = np.poly1d(z)
np.roots(p-1539)