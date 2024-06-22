# PyTorch Fundamentals


```python
# Import pytorch in our codespace
import torch
print(torch.__version__)
```

#### Output
```
2.3.0+cu121
```
    

2.3.0 is the pytorch version and 121 is the cuda version

Now you have already seen how to create a tensor in pytorch. In this notebook i am going to show you the operations which can be applied on a tensor with a quick previous revision.

### 1. Creating tensors

Scalar tensor ( a zero dimension tensor)

```python
scalar = torch.tensor(7)
print(scalar)
```

#### Output
```
tensor(7)
```
    
Check the dimension of the above tensor

```python
print(scalar.ndim)
```

#### Output
```
0
```
  
To retrieve the number from the tensor we use `item()`

```python
print(scalar.item())
```

#### Output
```
7
```
    
Vector (It is a single dimension tensor but contain many numbers)

```python
vector = torch.tensor([1,2])
print(vector)
```

#### Output
```
tensor([1, 2])
```    

Check the dimensions

```python
print(vector.ndim)
```

#### Output
```
1
```   

Check the shape of the vector

```python
print(vector.shape)
```

#### Output
```
torch.Size([2])
```
    

The above returns torch.Size([2]) which means our vector has a shape of [2]. This is because of the two elements we placed inside the square brackets ([1,2])

Note:
I'll let you in on a trick.

You can tell the number of dimensions a tensor in PyTorch has by the number of square brackets on the outside ([) and you only need to count one side.


```python
# Let's create a matrix
MATRIX = torch.tensor([[1,2],
                       [4,5]])
print(MATRIX)
```

#### Output
```
tensor([[1, 2],
            [4, 5]])
```    

There are two brackets so it must be 2 dimensions , lets check


```python
print(MATRIX.ndim)
```

#### Output
```
2
```    


```python
# Shape
print(MATRIX.shape)
```

#### Output
```
torch.Size([2, 2])
```    

It means MATRIX has 2 rows and 2 columns.

Let's create a TENSOR

```python
TENSOR = torch.tensor([[[1,2,3],
                        [4,5,6],
                        [7,8,9]]])
print(TENSOR)
```

#### Output
```
tensor([[[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]])
```    

Let's check the dimensions
```python
print(TENSOR.ndim)
```

#### Output
```
3
```    

shape
```python
print(TENSOR.shape)
```

#### Output
```
torch.Size([1, 3, 3])
```    

The dimensions go outer to inner.

That means there's 1 dimension of 3 by 3.

##### Let's summarise

* scalar -> a single number having 0 dimension.
* vector -> have many numbers but having 1 dimension.
* matrix -> a array of numbers having 2 dimensions.
* tensor -> a array of numbers having n dimensions.

### Random Tensors

We can create them using `torch.rand()` and passing in the `size` parameter.

Creating a random tensor of size (3,4)
```python 
rand_tensor = torch.rand(size = (3,4))
print(rand_tensor)
```

#### Output
```
tensor([[0.7462, 0.4950, 0.7851, 0.8277],
            [0.6112, 0.5159, 0.1728, 0.6847],
            [0.4472, 0.1612, 0.6481, 0.3236]])
```    

Check the dimensions

```python
print(rand_tensor.ndim)
```

#### Output
```
2
```    

Shape
```python
print(rand_tensor.shape)
```

#### Output
```
torch.Size([3, 4])
```    

Datatype
```python
print(rand_tensor.dtype)
```

#### Output
```
torch.float32
```    

### Zeros and ones

Here we will create a tensor of any shape filled with zeros and ones


```python
# Create a tensor of all zeros
zeros = torch.zeros(size = (3,4))
print(zeros)
```

#### Output
```
tensor([[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]])
```    

Create a tensor of ones
```python 
ones = torch.ones(size = (3,4))
print(ones)
```

#### Output
```
tensor([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]])
```    

### Create a tensor having range of numbers

You can use `torch.arange(start, end, step)` to do so.

Where:

* start = start of range (e.g. 0)
* end = end of range (e.g. 10)
* step = how many steps in between each value (e.g. 1)

> Note: In Python, you can use range() to create a range. However in PyTorch, torch.range() is deprecated show error, show use `torch.arange()`


```python
zero_to_ten = torch.arange(start = 0,
                           end = 10,
                           step = 1)
print(zero_to_ten)
```

#### Output
```
tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```    

# 2. Manipulating tensors (tensor operations)

The operations are :

* Addition
* Substraction
* Multiplication (element-wise)
* Division
* Matrix multiplication

### 1. Addition


```python
tensor = torch.tensor([1,2,3])
print(tensor+10)
```

#### Output
```
tensor([11, 12, 13])
```    

We have add 10 to each tensor element.


```python
tensor1 = torch.tensor([4,5,6])
print(tensor+tensor1)
```

#### Output
```
tensor([5, 7, 9])
```    

We have added two tensors , remember that addition takes place element wise.

### 2. Subtraction


```python
print(tensor-8)
```

#### Output
```
tensor([-7, -6, -5])
```    

We've subtracted 8 from the above tensor.


```python
print(tensor-tensor1)
```

#### Output
```
tensor([-3, -3, -3])
```    

### 3. Multiplication


```python
# Multiply the tensor with 10 (element wise)
print(tensor*10)
```

#### Output
```
tensor([10, 20, 30])
```    

Each element of tensor gets multiplied by 10.

Note:

PyTorch also has a bunch of built-in functions like `torch.mul()` (short for multiplication) and `torch.add()` to perform basic operations.


```python
# let's see them
print(torch.add(tensor,10))
```

#### Output
```
tensor([11, 12, 13])
```    


```python
print(torch.mul(tensor,10))
```

#### Output
```
tensor([10, 20, 30])
```    

### Matrix multiplication (is all you need)
One of the most common operations in machine learning and deep learning algorithms (like neural networks) is matrix multiplication.

PyTorch implements matrix multiplication functionality in the `torch.matmul()` method.

The main two rules for matrix multiplication to remember are:

The inner dimensions must match:
* (3, 2) @ (3, 2) won't work
* (2, 3) @ (3, 2) will work
* (3, 2) @ (2, 3) will work
The resulting matrix has the shape of the outer dimensions:
* (2, 3) @ (3, 2) -> (2, 2)
* (3, 2) @ (2, 3) -> (3, 3)


Note: "@" in Python is the symbol for matrix multiplication.


```python
# let's perform the matrix multiplication
tensor1 = torch.tensor([[[1,2,3],
                         [4,5,6],
                         [7,8,9]]])
tensor2 = torch.tensor([[[1,1,1],
                         [2,2,2],
                         [3,3,3]]])

print(tensor1) , print(tensor2)

```

#### Output
```
tensor([[[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]])
tensor([[[1, 1, 1],
             [2, 2, 2],
             [3, 3, 3]]])
```    

Let's check the shape
```python
print(tensor1.shape) , print(tensor2.shape)
```

#### Output
```
torch.Size([1, 3, 3])
torch.Size([1, 3, 3])
```

Matrix multiplication
```python 
print(torch.matmul(tensor1, tensor2))
```

#### Output
```
tensor([[[14, 14, 14],
             [32, 32, 32],
             [50, 50, 50]]])
```    

Can also use the "@" symbol for matrix multiplication, though not recommended
```python
print(tensor1 @ tensor2)
```

#### Output
```
tensor([[[14, 14, 14],
             [32, 32, 32],
             [50, 50, 50]]])
```    

Note:

If shape is not perfect you can transpose the tensor and perform the matrix multiplication.
