# Understanding the Neural Network

## Table of Contents
<details>
<summary>Click to expand</summary>

- [Introduciton](#introduction)
- [Neuron to Perceptron](#neuron-to-perceptron)
- [Key concepts](#key-concepts)
  - [Layers](#layers)
  - [Weights and Biases](#weights-and-biases)
  - [Activation Function](#activation-functions)
  - [Forward and Backward Pass](#forward-and-backward-propagation)
- [Implementation](#building-from-scratch)

</details>


## Introduction

This guide will walk you through a fundamental neural network implementation in Python. We'll build a `Neural Network` from scratch, allowing you to grasp the core concepts of how neural networks learn and make predictions.

### Let's start by Understanding the Basic Architecture of Neural Nets

## Neuron to Perceptron

| `Neuron` cells forming the humand nervous system | `Perceptron` inspired from human brain |
| :----------------------------------------------- | -------------------------------------: |
| Neurons are nerve cells that send messages all over your body to allow you to do everything from breathing to talking, eating, walking, and thinking. |  The perceptron is a mathematical model of a biological neuron. Performing heavy computations to think like humans. |
| Neuron collects signals from dendrites. | The first layer is knownn as Input Layer, acting like dendritres to receive the input signal. |
| Synapses are the connections between neurons where signals are transmitted. | Weights represent synapses. |
The axon terminal releases neurotransmitters to transmit the signal to other neurons. | The output is the final result – between 1 & 0, representing classification or prediction. |
---
> Human brain has a Network of Neurons, about 86 billion neurons and more than a 100 trillion synapses connections!


## **Key Concepts**

Artificial neurons are the fundamental processing units in an ANN. They receive inputs, multiply them by weights (representing the strength of connections), sum those weighted inputs, and then apply an activation function to produce an output.

### Layers
Neurons in ANNs are organized into layers:
* **Input Layer:** Receives the raw data.
* **(n) Hidden Layers:** (Optional) Intermediate layers where complex transformations occur. They learn to detect patterns and features in the data.
* **Output Layer:** Produces the final result (prediction or classification).

### Weights and Biases
- For each input $(x_i)$, a weight $(w_i)$ is associated with it. Weights, multiplied with input units $(w_i \cdot x_i)$, determine the influence of one neuron's output on another.
- A bias $(b_i)$ is added to help influence the end product, giving the equation as $(w_i \cdot x_i + b_i)$.
- During training, the network adjusts these weights and biases to minimize errors and improve its predictions.

### Activation Functions
- An activation function is applied to the result to introduce non-linearity in the model, allowing ANNs to learn more complex relationships from the data.
- The resulting equation: $y = f(g(x))$, determines whether the neuron will "fire" or not, i.e., if its output will be used as input for the next neuron.
- Common activation functions include the sigmoid function, tanh (hyperbolic tangent), and ReLU (Rectified Linear Unit).

### Forward and Backward Propagation
- **Flow of Information:** All the above steps are part of Forward Propagation. It gives the output equation as $y = f\left(\sum_{i=1}^n w_i x_i + b_i\right)$
- **Error Correction:** Backpropagation is the algorithm used to train ANNs by calculating the gradient of error at the output layer and then propagating this error backward through the network. This allows the network to adjust its weights and biases in the direction that reduces the error.
- The chain rule of calculus is the foundational concept to compute the gradient of the error:
  $
  \delta_{ij}(E) = \frac{\partial E}{\partial w_{ij}} = \frac{\partial E}{\partial \hat{y}_j} \cdot \frac{\partial \hat{y}_j}{\partial \theta_j} \cdot \frac{\partial \theta_j}{\partial w_{ij}}
  $
  where $E$ is the error, $\hat{y}_j$ is the predicted output, $\theta_j$ is the input to the activation function of the $j^{th}$ neuron, and $w_{ij}$ is the weight from neuron $i$ to neuron $j$.


## Building From Scratch

```python
# Import required libraries
import numpy as np
import matplotlib.pyplot as plt

class SimpleNeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Initialize weights and biases
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.bias_hidden = np.random.randn(hidden_size)
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_output = np.random.randn(output_size)
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        self.hidden_layer_input = np.dot(X, self.weights_input_hidden) + self.bias_hidden
        self.hidden_layer_output = self.sigmoid(self.hidden_layer_input)
        
        self.output_layer_input = np.dot(self.hidden_layer_output, self.weights_hidden_output) + self.bias_output
        self.output = self.sigmoid(self.output_layer_input)
        
        return self.output
    
    def backward(self, X, y, learning_rate):
        output_error = y - self.output
        output_delta = output_error * self.sigmoid_derivative(self.output)
        
        hidden_error = output_delta.dot(self.weights_hidden_output.T)
        hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_layer_output)
        
        self.weights_hidden_output += self.hidden_layer_output.T.dot(output_delta) * learning_rate
        self.bias_output += np.sum(output_delta, axis=0) * learning_rate
        self.weights_input_hidden += X.T.dot(hidden_delta) * learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0) * learning_rate
    
    def train(self, X, y, epochs, learning_rate):
        self.losses = []
        for epoch in range(epochs):
            self.forward(X)
            self.backward(X, y, learning_rate)
            loss = np.mean(np.square(y - self.output))
            self.losses.append(loss)
            if epoch % 1000 == 0:
                print(f"Epoch {epoch}, Loss: {loss}")
    
    def plot_loss(self):
        plt.plot(self.losses)
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.title('Training Loss Over Epochs')
        plt.show()
```

### Creating the Input & Output Array
Let's create a dummy input and outpu dataset. Here, the first two columns will be useful, while the rest might be noise.
```python
X = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [1]])
```

### Defining the Neural Network
With our input and output data ready, we'll define a simple neural network with one hidden layer containing three neurons.
```python
# neural network architecture
input_size = 2
hidden_layers = 1
hidden_neurons = [2] 
output_size = 1
```

### Visualizing the Training Loss
To understand how well our model is learning, let's visualize the training loss over epochs.
```python
model = NeuralNetwork(input_size, hidden_layers, hidden_neurons, output_size)
model.train(X, y, 100)
```
