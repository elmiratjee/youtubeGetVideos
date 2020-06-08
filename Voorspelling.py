import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model, preprocessing
from sklearn.utils import shuffle
from sklearn.linear_model import LinearRegression
import datetime as dt
import time
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style


data = pd.read_csv("dataset.csv", sep=";")
data = data[["Index", "videoPublishedAt"]]
data2 = data[["Index", "videoPublishedAt"]]

data2['videoPublishedAt'] = pd.to_datetime(data2['videoPublishedAt'], format='%d-%m-%Y %H:%M')
data2 = data2.assign(Dates=data['videoPublishedAt'])
data2 = data2.assign(IndexFloat=data['Index'])

le = preprocessing.LabelEncoder()
Index = le.fit_transform((data2["IndexFloat"]))

predict = "Date"

print(Index)

print(data2)

datums = pd.to_datetime(data2['videoPublishedAt'])
datums = data2['videoPublishedAt'].map(dt.datetime.toordinal)

print("dit is datums" + str(datums))

x = list([Index])
y = datums

print ("dit is x  " + str(x))
print ("dit is y  " + str(y))

x = np.array([Index])
print ("dit is x shape " + str(x.shape))
print ("dit is y shape " + str(y.shape))
x.shape[0] != y.shape[0]

y = y.values.reshape(1,-1)
print ("dit is y shape 2 " + str(y.shape))
model = LinearRegression()
model.fit(x, y)

x_predict = [50]
y_predict = model.predict(x_predict)

p1 = x
style.use("ggplot")
pyplot.scatter(data[p1], data[y])
pyplot.xlabel(p1)
pyplot.ylabel("test")
pyplot.show()