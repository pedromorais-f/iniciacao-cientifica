import tensorflow as tf
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt


def show_image(chosen_image):
    plt.figure()
    plt.imshow(chosen_image[0])
    plt.show()


print("Getting datasets...")
datasets = tf.keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = datasets.load_data()
print("Concluded\n")


print("Loading the model...")
loaded_model = load_model(filepath="../Fashion_Mnist/Model/model.h5")
print("Model loaded\n")

clothes = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

print("Showing ALL classes...")
for index, clothing in enumerate(clothes):
    print(f'{index}: {clothing}')
print("\n")

while True:
    index = input("Put a value(1 - 10000) or exit:")

    if index == "exit":
        break

    index = int(index)
    index -= 1
    image = x_test[index].reshape((1, 28, 28))
    show_image(image)

    print(f'Predict: {clothes[np.argmax(loaded_model.predict(image))]}')
    print(f'Result: {clothes[int(y_test[index])]}\n')
