from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

tbl = pd.read_csv("bmi.csv")

label = tbl["label"]
w = tbl["weight"] / 100
h = tbl["height"] / 200
wh = pd.concat([w, h], axis=1)
print(wh)

data_train, data_test, label_train, label_test = \
    train_test_split(wh, label)

clf = svm.SVC()
clf.fit(data_train, label_train)

predict = clf.predict(data_test)

as_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("accuracy_score =", as_score)
print("classification_report =", cl_report)
