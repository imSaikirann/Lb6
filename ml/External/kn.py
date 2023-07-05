from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import random
from sklearn.datasets import load_iris

iris_Data = load_iris()
label_Data = iris_Data.target_names;
for i in range(11):
    rn = random.randint(0,120)
    print(iris_Data.data[rn],"====>",label_Data[iris_Data.target[rn]])

X = iris_Data.data
y = iris_Data.target

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1)
print("lenght of training data is : ",len(X_train))
print("lenght of testing data is : ",len(X_test))

try:
    nn = int(input("enter neighbors:"))
    knn = KNeighborsClassifier(nn)
    knn.fit(X_train,y_train)

    test_data = input("Enter data:").split(",")
    for i in range(len(test_data)):
        test_data[i] = float(test_data[i])

    v = knn.predict([test_data])
    print(v)
    print("output is :",label_Data[v]);
except:
    print("invalid")
