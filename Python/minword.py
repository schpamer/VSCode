def find_short(s):
    s = s.split()
    l = len(min(s, key=len))
    return l # l: shortest word length
   
    print (l)

#%%
from sympy import *
x = symbols('x')
a = x**2+x-6
b = 2*x-12
a
factor(a)
solve(b,x)

#%%
solve(2*x-5=7)

#%%
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# function that returns dy/dt
def model(y,t):
    if t<10.0:
        u = 0
    else:
        u = 2
    dydt = (-y + u)/5.0
    return dydt

# initial condition
y0 = 1

# time points
t = np.linspace(0,400,1000)

# solve ODE
y = odeint(model,y0,t)

# plot results
plt.plot(t,y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()




#%%
