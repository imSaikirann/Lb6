from  sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
data = pd.read_csv('s.csv', names=['Message', 'Label'])
#adding another column labelnum ,based on the label adding 1 or 0
data['labelnum'] = data.Label.map({'pos':1,'neg':0}) 
print(data)
X = data["Message"]
Y = data.labelnum

Xtrain,Xtest,Ytrain,Ytest = train_test_split(X,Y)

count_vect = CountVectorizer()
Xtrain_dims = count_vect.fit_transform(Xtrain)
Xtest_dims = count_vect.transform(Xtest)

clf = MultinomialNB()

clf.fit(Xtrain_dims,Ytrain)

pre = clf.predict(Xtest_dims)

test_stmt = [input("Enter statement: ")]
test_dims = count_vect.transform(test_stmt)
pred = clf.predict(test_dims)

for stmt ,lbl in zip(test_stmt,pred):
    if lbl==1:
        print("pos")
    else:
        print("neg")

