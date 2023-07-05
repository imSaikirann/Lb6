import pandas as py
import numpy as np
import matplotlib.pyplot as plt

data = py.read_csv('l.csv')
age = data['Age']
income = data['Income']

agesize = np.size(age)
agemean = np.mean(age)
incomemean = np.mean(income)

CD_ageincome = np.sum(age*income)-agesize*agemean*incomemean
CD_ageage = np.sum(age*age)-agesize*agemean*agemean

b1 = CD_ageincome/CD_ageage
b0 =incomemean-b1*agemean
print("b1=",b1,"b0=",b0);

plt.scatter(age,income, color="b" ,marker="o")
res_vector = b0+b1*age
plt.plot(age,res_vector,color="r")
plt.xlabel('age')
plt.ylabel('income')
plt.show()