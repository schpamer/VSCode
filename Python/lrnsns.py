import seaborn as sns
import pandas as pf
import matplotlib.pyplot as plt 

tips = sns.load_dataset('tips') #!do not call a file seaborn or this breaks


df = tips.head()
print(df)
#sns.distplot(tips['total_bill'],kde=False,bins=40)
#plt.show()  #need this from matplotlib to display and work

#other kind = reg(regression) and kde
#sns.jointplot(x='total_bill',y='tip',data=tips,kind='kde')

sns.pairplot(tips)
plt.show()