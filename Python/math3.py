#%%
import numpy as np 
from sympy import *
#from __future__ import division the / and /= operators are translated to true division opcodes; otherwise they are translated to classic division (until Python 3.0 comes along, where they are always translated to true division).

# declare symbols for common use
#%%
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

# Integrate functions below

#y = ((sin(x))**2,0,pi/4)
##y =  x**2 + x + 1
#print(y)
#z = integrate(y,x)
#pprint(z)

# Limits of equation
#y = (1/x)
#pprint(y)
#z = limit(y,x,00)  #two consecutive 0's for infinity
#print(z)

# Derivitaves function
#y =  x**2 + x + 1
#print(y)
#z = diff(y,x)
#pprint(z)

#solve for single and multiple variables
#Math 3 EOC #1

#%%
from sympy import *
y =  x**2 + 2*x + 2
print(y)
z = solve(y,x)
pprint(z)


y = (x**3 + x**2 - 16*x - 16)
z = factor(y)
pprint(z)
y=y
print(y)
y=((x+y)**2)
z=expand(y)
pprint(z)

#%%
