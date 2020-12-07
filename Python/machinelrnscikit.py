import numpy as np 
from sympy import *

#from sklearn.model_selection import train_test_split
#from sklearn import datasets
#from sklearn import svm

#X, y = np.arange(10).reshape((5,2)), range(5)
#X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3)


#print(X_train)
#print(y_train)
#print(X_test)
x = Symbol('x')
y = (x/(x**2+2*x+1))
#y = (sin**2*x,0,pi/4)
print(y)
z = integrate(y,x)
print(z)
