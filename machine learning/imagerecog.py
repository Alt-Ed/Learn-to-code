#importing essentials libraries 
import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
(X_train, y_train), (X_test,y_test) = datasets.cifar10.load_data()
X_train.shape
X_test.shape
y_train.shape

y_train[:5]
y_train = y_train.reshape(-1,)
y_train[:5]

y_test = y_test.reshape(-1,)
classes = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]
plot_sample(X_train, y_train, 0)
plot_sample(X_train, y_train, 1)

plot_sample(X_train, y_train, 5)
#normalizing the data
X_train = X_train / 255.0
X_test = X_test / 255.0

cnn = models.Sequential([
    layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
  #Filters are used to extract features from images in the process of convolution
  #kernel_size: An integer or tuple/list of 2 integers, specifying the height and width of the 2D convolution window.
  # Can be a single integer to specify the same value for all spatial dimensions.  
    layers.Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

cnn.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

cnn.fit(X_train, y_train, epochs=10)

cnn.evaluate(X_test,y_test)
y_pred = cnn.predict(X_test)
y_pred[:5]y_classes = [np.argmax(element) for element in y_pred]
y_classes[:5]
y_test[:5]
plot_sample(X_test, y_test,3)
classes[y_classes[3]]              