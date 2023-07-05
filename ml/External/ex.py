from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv('s.csv',names=["message","Label"])
data['labelnum'] = data.Label.map({'pos':1 ,'neg':0})
print(data)

X = data["message"]
Y = data.labelnum

Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,Y)
count_v = CountVectorizer()
Xtrain_dims = count_v.fit_transform(Xtrain)
Xtest_dims = count_v.transform(Xtrain)

clf = MultinomialNB()
clf.fit(Xtrain_dims,Ytrain)
pre = clf.predict(Xtest_dims)

test_data = [input("enter:")]
test_dims = count_v.transform(test_data)
v = clf.predict(test_dims)

for stmt,lbl in zip(test_dims,v):
    if lbl == 1:
        print("pos")
    else:
        print("neg")