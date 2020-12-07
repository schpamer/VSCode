#%%import numpy as np 
x = np.arange(0,100)
y = x*2
z = 3*(x**2) +2

import matplotlib.pyplot as plt 

#fig = plt.figure()

#ax1 = fig.add_axes([0.1,0.1,1,1])
#ax1.plot(x,y,color='red')
#ax2 = fig.add_axes([0.2,0.5,.2,.2])
#ax1.set_title('title')
#ax1.set_xlabel('x')
#ax1.set_ylabel('y')#
#ax1.set_ylim(0,280)

#ax2.plot(x,z,color='purple')
#x2.set_title('title')
#ax2.set_xlabel('x')
#ax2.set_ylabel('y')
#plt.show()
#f, (ax1, ax2) = plt.subplots(1,2)
#ax1.plot(x,y,color='blue',ls='--')
#ax1.set_title('X v Y')

#ax2.plot(x,z,color='red',lw=3)
#ax2.set_title('X vs Z')


#plt.show()

f, (ax1, ax2) = plt.subplots(1,2,figsize=(12,2))
ax1.plot(x,y,color='blue',lw=3)
ax1.set_title('X v Y')

ax2.plot(x,z,color='red',ls='--')
ax2.set_title('X vs Z')


plt.show()#

# %%


