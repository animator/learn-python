# CNN

A convolutional neural network, or CNN for short, is a type of classifier

A CNN is a neural network: an algorithm used to recognize patterns in data. Neural Networks in general are composed of a collection of neurons that are organized in layers, each with their own learnable weights and biases. Let’s break down a CNN into its basic building blocks.

1. **Tensor**: A tensor can be thought of as an n-dimensional matrix. In the CNN above, tensors will be 3-dimensional with the exception of the output layer.
2. **Neuron**: A neuron can be thought of as a function that takes in multiple inputs and yields a single output.
3. **Layer**: A layer is simply a collection of neurons with the same operation, including the same hyperparameters.
4. **Kernel weights and biases**: While unique to each neuron, are tuned during the training phase, and allow the classifier to adapt to the problem and dataset provided. 

## Hyperparameters in a CNN Model

1. **Padding**: Padding is often necessary when the kernel extends beyond the activation map. Padding conserves data at the borders of activation maps, which leads to better performance, and it can help preserve the input's spatial size, which allows an architecture designer to build deeper, higher performing networks. There exist many padding techniques, but the most commonly used approach is zero-padding because of its performance, simplicity, and computational efficiency. The technique involves adding zeros symmetrically around the edges of an input.
2. **Kernel size**: Often also referred to as filter size, refers to the dimensions of the sliding window over the input. Choosing this hyperparameter has a massive impact on the image classification task. For example, small kernel sizes are able to extract a much larger amount of information containing highly local features from the input. A smaller kernel size also leads to a smaller reduction in layer dimensions, which allows for a deeper architecture. Conversely, a large kernel size extracts less information, which leads to a faster reduction in layer dimensions, often leading to worse performance.
3. **Stride**: Stride indicates how many pixels the kernel should be shifted over at a time. Which means that the dot product is performed on a 3x3 window of the input to yield an output value, then is shifted to the right by one pixel for every subsequent operation. The impact stride has on a CNN is similar to kernel size. As stride is decreased, more features are learned because more data is extracted, which also leads to larger output layers. On the contrary, as stride is increased, this leads to more limited feature extraction and smaller output layer dimensions.

## Activation Functions

1. **ReLU**: 
   \[
   ReLU(x) = \max(0, x)
   \]
   ReLU applies much-needed non-linearity into the model. Non-linearity is necessary to produce non-linear decision boundaries, so that the output cannot be written as a linear combination of the inputs. The ReLU activation function is specifically used as a non-linear activation function, as opposed to other non-linear functions such as Sigmoid because it has been empirically observed that CNNs using ReLU are faster to train than their counterparts.

2. **Softmax**: A softmax operation serves a key purpose: making sure the CNN outputs sum to 1. Because of this, softmax operations are useful to scale model outputs into probabilities.
   \[
   Softmax(x_i) = \frac{\exp(x_i)}{\sum \exp(x_j)}
   \]
   
## Some important parameters

1. **Epoch** – The number of times the algorithm runs on the whole training dataset.
2. **Sample** – A single row of a dataset.
3. **Batch** – It denotes the number of samples to be taken to for updating the model parameters.
4. **Learning rate** – It is a parameter that provides the model a scale of how much model weights should be updated.
5. **Cost Function/Loss Function** – A cost function is used to calculate the cost, which is the difference between the predicted value and the actual value.
6. **Optimizers**:It is a crucial element that fine-tunes a neural network’s parameters during training. Its primary role is to minimize the model’s error or loss function, enhancing performance.

## Different layer of the CNN

- **Input Layer**: The input layer (leftmost layer) represents the input image into the CNN. Because we use RGB images as input, the input layer has three channels, corresponding to the red, green, and blue channels, respectively, which are shown in this layer.

- **Pooling Layers**: There are many types of pooling layers in different CNN architectures, but they all have the purpose of gradually decreasing the spatial extent of the network, which reduces the parameters and overall computation of the network.

- **Flatten Layer**: This layer converts a three-dimensional layer in the network into a one-dimensional vector to fit the input of a fully-connected layer for classification. For example, a 5x5x2 tensor would be converted into a vector of size 50. The previous convolutional layers of the network extracted the features from the input image, but now it is time to classify the features. We use the softmax function to classify these features, which requires a 1-dimensional input. This is why the flatten layer is necessary.

- **Dense layer**:A dense layer is a layer where each neuron is connected to every neuron in the previous layer. In other words, the output of each neuron in a dense layer is computed as a weighted sum of the inputs from all the neurons in the previous layer.

## An Example CNN Model for Multiclass Classification

```python

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

#call the sequential api
model = Sequential()
tf.random.set_seed(42)

#3 Conv2D layers with kernel size 3*3
#3 MaxPooling layers of kernel sie 3*3
#Dense layer with 100 hidden neurons as input layer
model.add(Dense(100, input_shape=[100, 100, 100, 3], activation='relu'))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))

model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))

model.add(Flatten())

#Output layer for 20 different classes for classification
model.add(Dense(20, activation='softmax'))

model.compile(optimizer='Adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(X, y, epochs=15, validation_split=0.2)

# Define the input shape of the model
model.build(input_shape=[100, 100, 100, 3])

# Call the summary() method on the model
model.summary()

```
# Model Summary: sequential_1

## Model Architecture

| Layer (type)          | Output Shape        | Param # |
|-----------------------|---------------------|---------|
| conv2d_21 (Conv2D)    | (100, 98, 98, 32)   | 896     |
| max_pooling2d_21      | (100, 49, 49, 32)   | 0       |
| (MaxPooling2D)        |                     |         |
| conv2d_22 (Conv2D)    | (100, 47, 47, 32)   | 9248    |
| max_pooling2d_22      | (100, 23, 23, 32)   | 0       |
| (MaxPooling2D)        |                     |         |
| conv2d_23 (Conv2D)    | (100, 21, 21, 32)   | 9248    |
| max_pooling2d_23      | (100, 10, 10, 32)   | 0       |
| (MaxPooling2D)        |                     |         |
| flatten_7 (Flatten)   | (100, 3200)         | 0       |
| dense_12 (Dense)      | (100, 100)          | 320100  |
| dense_13 (Dense)      | (100, 22)           | 2222    |

## Total Parameters
- **Trainable params:** 341,714 (1.30 MB)
- **Non-trainable params:** 0 (0.00 Byte)

