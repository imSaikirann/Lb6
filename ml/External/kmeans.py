from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1.713,1.202],[0.123,2.102]])
y = np.array([0,1])

kmeans = KMeans(n_clusters=2,random_state=0).fit(X,y)
i=0;
for v in X:
    print(v[0],"\t", v[1],y[i])
    i = i+1;

print("-"*20)

print("Enter input:")
 
test_data=[]
v1 = float(input("enter var 1:"))
v2 = float(input("enter var 2:"))
test_data.append(v1)
test_data.append(v2)
output = kmeans.predict([test_data])
print(output)

