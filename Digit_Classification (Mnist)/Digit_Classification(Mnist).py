# -*- coding: utf-8 -*-
"""ANN_Mnist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aF8vEKttd8D-aaSuJjrSgU9ZYdlIO3ge

Importing Libraries
"""

from tensorflow import keras
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.callbacks import EarlyStopping

"""Loading Dataset directly into Train & Test parameters"""

(X_train,Y_train),(X_test,Y_test) = keras.datasets.mnist.load_data()

"""Getting to know the data

"""

X_train.shape

X_train[0]

# Plotting the image of the 1st row to see how it looks and what digit it is (5)
import matplotlib.pyplot as plt
plt.imshow(X_train[0])

Y_train[0]

"""The values are divided by 255 to standardize them since colors have a range of 0 to 255."""

X_train = X_train/255
X_test = X_test/255

X_train[0]

# Obj
ann = Sequential()

# Hidden layers
ann.add(Flatten(input_shape=(28,28)))   # Here the image is of (28 x 28) pixels i.e. 28D so using flattening layer to convert it into 1D array 
ann.add(Dense(128,activation="relu"))   
ann.add(Dense(32,activation="relu"))

# Output layers
ann.add(Dense(10,activation="softmax"))   # As in total possibilities are [0,1,2...8,9] so total neurons are 10 , Softmax is used for multiclass classififcation  

# diagram
ann.summary()

ann.compile(loss="sparse_categorical_crossentropy",optimizer="adam",metrics=["accuracy"])

"""Creating an object of early stopping to save the resources"""

ES = EarlyStopping(mode="min",monitor="val_loss",patience=25,verbose=1)

ann.fit(X_train,Y_train,validation_split=0.2,epochs=25,batch_size=64,callbacks=ES)

Y_prob = ann.predict(X_test)

"""Assigning the class based on the highest probability values for the numbers 0 to 9."""

Y_pred = Y_prob.argmax(axis=1)

"""The probability that the first row belongs to each of the [0-9] classes."""

Y_prob[0]

Y_pred

"""Classification Report"""

# Scores of all classes are pretty good so we can say model has learnt well on all the classes
from sklearn.metrics import classification_report
print(classification_report(Y_test,Y_pred))

