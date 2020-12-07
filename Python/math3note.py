#%%
import numpy as np
from sympy import *
import cv2
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

#%%
print(np.__version__)
print(cv2.__version__)
init_printing(use_latex=True)


#%%
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)


#%%
expr = integrate(x**2 + x + 1,x)
expr
#pprint(expr)

#%%
expr = diff(y,x)
expr
#pprint(z)

#%%
expr = (x+y)**3
expr


#%%
I
I**2

#%%
expr = Rational(1,3)+ Rational(1,2)
N(expr)

#%%
N(pi,100)


#%%
expr = pi*x**2
expr

#%%
expr.subs(x,3)

#%%
N(_)

#%%
expr = (x+y)**2
expand(expr)

#%%
factor(_)

#%%
expr = (2*x + Rational(1,3)*x + 4) / x
expr

#%%
Integral(sin(x), (x,0,pi))

#%%
N(_)

#%%
expr = Sum(1/(x**2+2*x), (x,1,10))
expr

#%%
N(_)

#%%
expr_1 = 2*x + y
expr_2 = 2*y - x - 5
solve([expr_1,expr_2],(x,y))

#%%
expr = sin(2*sin(x**3))
plot(expr,(x,0,5));

#%%
list1 = np.arange(1,1000)
list2 = pd.Series(list1)


#%%
expr = x**3 + sqrt(3)*x - Rational(1,3)
lf = lambdify(x, expr)


#%%
%timeit lf(list1)
%timeit lf(list2)

#%%
## The Plot
fig = plt.figure()
axis = fig.add_subplot(111)

x_vals = np.linspace(-5.,5)
y_vals = lf(x_vals)

axis.grid()
axis.plot(x_vals,y_vals)

plt.show();

#%%
x = np.linspace(0, 20, 100)
plt.plot(x, (1/x))
plt.show() 

#%%
M = eye(4)
M

#%%
x1, x2, x3, x4, x5 = symbols('x1, x2, x3,x4,x5')
M1 = Matrix([[0,0,0,1,-1,35],[1,1,0,0,0,85],[1,0,1,0,0,75],[0,1,-1,1,0,70],[0,0,0,0,1,25]])
M1
#M2 = ([35,85,75,70,25])
M1.rref()
##this actually works can use at will

#%%
M = Matrix([[1,2,3,4],[2,1,2,3],[5,5,1,0]])
M
M.rref()

#%%
A = np.array([ [3,4], [-1,2] ])
b = np.array([-23,-19])
z = np.linalg.solve(A,b)
print(z)

#%%
A = np.array([ [1,1], [1,2] ])
b = np.array([-9,-25])
z = np.linalg.solve(A,b)
print(z)


#%%
M = np.array([ [1,-2,-1], [2,2,-1], [-1,-1,2] ])
c = np.array([6,1,1])
y = np.linalg.solve(M,c)
print(y)

#%%
import sympy as sym
sym.init_printing()
x,y,z = sym.symbols('x,y,z')
c1 = sym.Symbol('c1')
f = sym.Eq(2*x**2+y+z,1)
g = sym.Eq(x+2*y+z,c1)
h = sym.Eq(-2*x+y,-z)

sym.solve([f,g,h],(x,y,z))


#%%
import ipywidgets as wg
from IPython.display import display 

myName = wg.Text(value='Name')
myAge = wg.IntSlider(description='Age:')
display(myName,myAge)

### new cell
print(myName.value + ' is ' + str(myAge.value) + ' years old')


#%%
x = quadratic(4,5,1)
x

#%%
import cmath

a = 3
b = 5
c = 2
# Discriminent
d = (b**2) - (4*a*c)
root1 = (-b - cmath.sqrt(d)) / (2 * a)
root2 = (-b + cmath.sqrt(d)) / (2 * a)
print(root1)
print(root2)

#%%
#from scipy.constants import pi
import math

print(pi)
print(math.e)
print(math.fabs(-20.5))
print(math.factorial(15))
print(math.gcd(8,35))
print(math.pow(3,10))
print(math.degrees(pi/2))

#%%
