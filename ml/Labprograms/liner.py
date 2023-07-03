import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_Frame = pd.read_csv('Lcsv.csv')
age = data_Frame['Age']
income = data_Frame['Income']

agesize = np.size(age)
mean_age = np.mean(age)
mean_income = np.mean(income)


CD_ageincome = np.sum(age*income)-agesize*mean_age*mean_income
CD_ageage = np.sum(age*age)-agesize*mean_age*mean_age

b1 = CD_ageincome/CD_ageage
b0 = mean_income-b1*mean_age

print("coefficents are:")
print("b1=",b1,"b0=",b0)
plt.scatter(age,income, color="p",marker="o")
res_vector = b0+b1*age
plt.plot(age,res_vector, color="r")
plt.xlabel('age')
plt.ylabel('income')
plt.show()

