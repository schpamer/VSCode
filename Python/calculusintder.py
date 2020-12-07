#%%
import numpy as np 
from sympy import *
#from __future__ import division the / and /= operators are translated to true division opcodes; otherwise they are translated to classic division (until Python 3.0 comes along, where they are always translated to true division).

# declare symbols for common use
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

# Integrate functions below

y = ((sin(x))**2,0,pi/4)
#y =  x**2 + x + 1
print(y)
z = integrate(y,x)
pprint(z)

# Limits of equation
y = (1/x)
pprint(y)
z = limit(y,x,00)  #two consecutive 0's for infinity
print(z)

# Derivitaves function
y =  x**2 + x + 1
print(y)
z = diff(y,x)
pprint(z)

#solve for single and multiple variables
y =  x**2 + x + 1
print(y)
z = solve(y,x)
pprint(z)
y=y
z = solve([x + 5*y - 2, -3*x + 6*y - 15], [x, y])
print(z)
# %%
