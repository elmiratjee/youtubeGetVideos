import keras
import tensorflow as tf
import pandas as pd
from sklearn import linear_model, preprocessing
import datetime as dt
from keras.optimizers import adam
import matplotlib.pyplot as pyplot
from matplotlib import style



data = pd.read_csv("dataset2.csv", sep=";")
data = data[["Index", "videoPublishedAt"]]
data2 = data[["Index", "videoPublishedAt"]]

data2['videoPublishedAt'] = pd.to_datetime(data2['videoPublishedAt'], format='%d-%m-%Y %H:%M')
data2 = data2.assign(Dates=data['videoPublishedAt'])
data2 = data2.assign(IndexFloat=data['Index'])

le = preprocessing.LabelEncoder()
Index = le.fit_transform((data2["IndexFloat"]))

datums = pd.to_datetime(data2['videoPublishedAt'])
datums = data2['videoPublishedAt'].map(dt.datetime.toordinal)


model = keras.Sequential([
    keras.layers.Dense(64, activation=tf.nn.relu, input_shape=[1]),
    keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(1)
])

#optimizer = tf.keras.optimizers.RMSprop(0.001)
opt = adam(lr=0.001, decay=1e-6)

model.compile(loss='mean_squared_error',
              optimizer=opt,
              metrics=['mean_absolute_error', 'mean_squared_error'])

model.fit(Index, datums, epochs=50000)

model.predict([50])
endResult = model.predict([50])

print(endResult)
endResult = int(endResult)
print(endResult)


endResultDatum = dt.datetime.fromordinal(endResult)
print("Eind resultaat " + str(endResultDatum))

