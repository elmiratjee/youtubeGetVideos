import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
from sklearn.linear_model import LinearRegression
import datetime as dt
import time
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style

data = pd.read_csv("dataset.csv", sep=";")

data = data[["Index", "videoPublishedAt"]]
data['videoPublishedAt'] = pd.to_datetime(data['videoPublishedAt'])
data['videoPublishedAt']=data['videoPublishedAt'].map(dt.datetime.toordinal)

predict = "videoPublishedAt"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y)

best = 0
for besttrain in range(50):
    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    accuracy = linear.score(x_test, y_test)
    print(accuracy)

    if accuracy > best:
        best = accuracy
        with open("dataset.pickle", "wb") as f:
            pickle.dump(linear, f)

print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])
p1 = "Index"
style.use("ggplot")
pyplot.scatter(data[p1], data["videoPublishedAt"])
pyplot.xlabel(p1)
pyplot.ylabel("Dates")
pyplot.show()