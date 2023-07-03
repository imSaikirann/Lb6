from sklearn.cluster import KMeans
import numpy as np

X = np.array([[1.713,1.586], [0.180,1.786], [0.353,1.240],
[0.940,1.566], [1.486,0.759], [1.266,1.106],[1.540,0.419],[0.459,1.799],[0.773,0.186]])
y=np.array([0,1,1,0,1,0,1,1,1])

kmeans = KMeans(n_clusters=3,random_state=0).fit(X,y)

print("The input datais ")
print("VAR1\tVAR2\tClass")
i=0
for v in X:
    print(v[0],"\t",v[1],y[i])
    i=i+1

print("="*10)
print("Enter your test input")
test_data=[]
v1 = float(input("Enter var1:"))
v2 = float(input("Enter var2:"))
test_data.append(v1)
test_data.append(v2)
print(kmeans.predict([test_data]))

