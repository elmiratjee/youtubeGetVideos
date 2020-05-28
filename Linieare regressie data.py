import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import datetime as dt

data = pd.read_csv("dataset.csv", sep=";")

data = data[["Index", "videoPublishedAt"]]
data['videoPublishedAt'] = pd.to_datetime(data['videoPublishedAt'])
data['videoPublishedAt']=data['videoPublishedAt'].map(dt.datetime.toordinal)

predict = "videoPublishedAt"

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)
accuracy = linear.score(x_test, y_test)
print(accuracy)

print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)

predictions = linear.predict(x_test)
for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])
