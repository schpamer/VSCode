#%%
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import dlib
from PIL import Image
%matplotlib inline
%use_local_mathjax()

#%%
arr = np.ones((5,5))
cv2.__version__

#%%
arr = arr/2
arr

#%%
np.random.seed(101)
arr = np.random.randint(low=0,high=100,size=(5,5))
arr

#%%
arr.max()

#%%
arr.min()

#%%
img1 = Image.open('sammy.jpg')

#%%
img1.show()

#%%
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)


#%%
expr = integrate(x**2 + x + 1,x)
expr

#%%
y = 3*x**4+2*x+1
expr = diff(y,x)
expr

#%%
N(pi,100)


#%%
expr = pi*x**2
expr

#%%
expr = (x+y)**2
expand(expr)

#%%
expr = Integral(sin(x), (x,0,pi))
expr

#%%
N(expr)

#%%
expr_1 = 2*x + y
expr_2 = 2*y - x - 5
solve([expr_1,expr_2],(x,y))


#%%
expr = sin(2*sin(x**3))
plot(expr,(x,0,5));

#%%
expr = x**3 + sqrt(3)*x - Rational(1,3)
lf = lambdify(x, expr)

#%%
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
# Limits of equation
y = (1/x)
pprint(y)
z = limit(y,x,00)  #two consecutive 0's for infinity
print(z)

#%%
y = (x**3 + x**2 - 16*x - 16)
z = factor(y)
print(z)

#%%
len("SpamIamI3!!")

#%%
print("Hello")


#%%
len("hello")

#%%
