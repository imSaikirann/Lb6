from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import random
from sklearn.datasets import load_iris

irisData = load_iris()

label_dataset = irisData.target_names
print("Sample")

for i in range(11):
    rn = random.randint(0, 120)
    print(irisData.data[rn], "==>", label_dataset[irisData.target[rn]])

X = irisData.data
y = irisData.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

print("The Training dataset length:", len(X_train))
print("The Testing dataset length:", len(X_test))

try:
    nn = int(input("Enter the number of neighbors: "))
    knn = KNeighborsClassifier(nn)
    knn.fit(X_train, y_train)

    test_data = input("Enter data: ").split(",")
    test_data = [float(val) for val in test_data]

    v = knn.predict([test_data])
    print("Output is:", label_dataset[v])

except ValueError:
    print("Invalid input. Please enter numeric values.")
except Exception as e:
    print("An error occurred:", str(e))
