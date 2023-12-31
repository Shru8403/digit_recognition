# -*- coding: utf-8 -*-
"""handwritten.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16uNvVd4ZlRwIFU2xU8H6HQ-oMtCLuOiJ
"""

# Libraries
import os
import cv2
import numpy as np
import matplotlib.pyplot as matp
import tensorflow as tensor

# Loading dataset
mnist = tensor.keras.datasets.mnist

(x_training_data,y_training_data),(X,Y) = mnist.load_data()


x_training_data = tensor.keras.utils.normalize(x_training_data,axis=1)
X = tensor.keras.utils.normalize(X,axis=1)

# Adding layers
model = tensor.keras.models.Sequential()
model.add(tensor.keras.layers.Flatten(input_shape=(28,28)))
model.add(tensor.keras.layers.Dense(128, activation='relu'))
model.add(tensor.keras.layers.Dense(128, activation='relu'))
model.add(tensor.keras.layers.Dense(10, activation='softmax'))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

model.fit(x_training_data,y_training_data, epochs = 3)

model.save('handwritten.model')

# Reading digits
for x in range(1,4):

    image=cv2.imread(f'{x}.png')[:,:,0]
    image=np.invert(np.array([image]))
    prediction=model.predict(image)
    print("================================= \n")
    print("The number in the image is : ",np.argmax(prediction))
    print("================================= \n")
    matp.imshow(image[0],cmap=matp.cm.binary)
    matp.show()