# Exercício trapézio 1
import numpy as np
import matplotlib.pyplot as plt
def trapezio(f,a,b,N):
    
    x = np.linspace(a,b,N+1) # N+1 pontos
    y = f(x)
    y_inter = y[1:N] # todos valores menos o primeiro e o ultimo
    dx = (b - a)/N
    T = (dx)*np.sum(y_inter)+(dx/2)*(y[0]+y[N])
    return T

trapezio(lambda x:((x+3)/(x**2 -1)),2,10,4)

# Exercício simpson - 2
import numpy as np
# Define function to integrate
def f(x):
    return ((x+3)/(x**2 -1))

# Implementing Simpson's 1/3 
def simpson(x0,xn,n):
    # calculating step size
    h = (xn - x0) / n
    
    # Finding sum 
    integration = f(x0) + f(xn)
    
    for i in range(1,n):
        k = x0 + i*h
        
        if i%2 == 0:
            integration = integration + 2 * f(k)
        else:
            integration = integration + 4 * f(k)
    
    # Finding final integration value
    integration = integration * h/3
    
    return integration

result = simpson(2, 10, 4)
print("Integracao resultado por Simpson é: %0.6f" % (result) )

#Exercício usando squad
import scipy.integrate as si
f= lambda x:((x+3)/(x**2 -1))
i = si.quad(f, 2, 10)
print (i)