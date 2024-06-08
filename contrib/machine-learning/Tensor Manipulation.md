# Reshaping, stacking, squeezing and unsqueezing the tensors

Sometime we often need to change the shape , adding the new dimension and removing the dimension from the tensors without changing the values inside them.

To do so, some popular methods are:

| Method | One-line description |
| ----- | ----- |
| [`torch.reshape(input, shape)`](https://pytorch.org/docs/stable/generated/torch.reshape.html#torch.reshape) | Reshapes `input` to `shape` (if compatible), can also use `torch.Tensor.reshape()`. |
| [`torch.stack(tensors, dim=0)`](https://pytorch.org/docs/1.9.1/generated/torch.stack.html) | Concatenates a sequence of `tensors` along a new dimension (`dim`), all `tensors` must be same size. |
| [`torch.squeeze(input)`](https://pytorch.org/docs/stable/generated/torch.squeeze.html) | Squeezes `input` to remove all the dimenions with value `1`. |
| [`torch.unsqueeze(input, dim)`](https://pytorch.org/docs/1.9.1/generated/torch.unsqueeze.html) | Returns `input` with a dimension value of `1` added at `dim`. |

## 1. Reshaping


```python
import torch
```


```python
# Create a tensor
tensor = torch.arange(1,20,2)
tensor
```




    tensor([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])




```python
# Checking the shape
tensor.shape
```




    torch.Size([10])




```python
# Reshaping the shape
torch.reshape(tensor , shape = (2,3))
```


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-7-13f0e8c7b94d> in <cell line: 2>()
          1 # Reshaping the shape
    ----> 2 torch.reshape(tensor , shape = (2,3))
    

    RuntimeError: shape '[2, 3]' is invalid for input of size 10


Note: It is showing error because shape (2,3) is invalid for size 10 because (2,3) means having total 2*3 i.e 6 elements but there are 10.

So always select that shape which can be compitable with the size.

for above we can use the following shapes:

  * 2*5
  * 5*2
  * 1*10
  * 10*1

  Here it means `rows*columns`


```python
torch.reshape(tensor , shape=(2,5))
```




    tensor([[ 1,  3,  5,  7,  9],
            [11, 13, 15, 17, 19]])




```python
torch.reshape(tensor , shape = (5,2))
```




    tensor([[ 1,  3],
            [ 5,  7],
            [ 9, 11],
            [13, 15],
            [17, 19]])




```python
torch.reshape(tensor , shape = (1,10))
```




    tensor([[ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19]])




```python
tensor
```




    tensor([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])




```python
torch.reshape(tensor , shape = (10,1))
```




    tensor([[ 1],
            [ 3],
            [ 5],
            [ 7],
            [ 9],
            [11],
            [13],
            [15],
            [17],
            [19]])



We can also use `torch.Tensor.reshape()` for the same!


```python
torch.Tensor.reshape(tensor , shape = (2,5))
```




    tensor([[ 1,  3,  5,  7,  9],
            [11, 13, 15, 17, 19]])



Note:  Reshape() makes a copy of the original tensor not change its content.

## 2. Stacking

Concatenates a sequence of tensors along a new dimension.



```python
t1 = torch.rand(2,3)
t1
```




    tensor([[0.6487, 0.9401, 0.6886],
            [0.8676, 0.2468, 0.6775]])




```python
t1.ndim , t1.size()
```




    (2, torch.Size([2, 3]))




```python
t2 = torch.tensor([[1,2,3],
                   [4,5,6]])
t2
```




    tensor([[1, 2, 3],
            [4, 5, 6]])




```python
t2.ndim , t2.size()
```




    (2, torch.Size([2, 3]))




```python
# Let's stack
t_stack = torch.stack((t1,t2))  # By default it stacks alon the 0th dimension.
t_stack
```




    tensor([[[0.6487, 0.9401, 0.6886],
             [0.8676, 0.2468, 0.6775]],
    
            [[1.0000, 2.0000, 3.0000],
             [4.0000, 5.0000, 6.0000]]])




```python
torch.stack((t1,t2),dim = 1)
```




    tensor([[[0.6487, 0.9401, 0.6886],
             [1.0000, 2.0000, 3.0000]],
    
            [[0.8676, 0.2468, 0.6775],
             [4.0000, 5.0000, 6.0000]]])




```python
torch.stack((t1,t2), dim = 2)
```




    tensor([[[0.6487, 1.0000],
             [0.9401, 2.0000],
             [0.6886, 3.0000]],
    
            [[0.8676, 4.0000],
             [0.2468, 5.0000],
             [0.6775, 6.0000]]])



## 3. Squeeze

How about removing all single dimensions from a tensor?

To do so you can use `torch.squeeze()` (I remember this as *squeezing* the tensor to only have dimensions over 1).


```python
# let's create tensor
x = torch.tensor([[1,2,3,4,5]])
```


```python
print(f"Previous tensor: {x}")
print(f"Previous shape: {x.shape}")

# Remove extra dimension from x_reshaped
x_squeezed = x.squeeze()
print(f"\nNew tensor: {x_squeezed}")
print(f"New shape: {x_squeezed.shape}")
```

    Previous tensor: tensor([[1, 2, 3, 4, 5]])
    Previous shape: torch.Size([1, 5])
    
    New tensor: tensor([1, 2, 3, 4, 5])
    New shape: torch.Size([5])
    

## 4. Unsqueeze

And to do the reverse of `torch.squeeze()` you can use `torch.unsqueeze()` to add a dimension value of 1 at a specific index.


```python
print(f"Previous tensor: {x_squeezed}")
print(f"Previous shape: {x_squeezed.shape}")

## Add an extra dimension with unsqueeze
x_unsqueezed = x_squeezed.unsqueeze(dim=0)
print(f"\nNew tensor: {x_unsqueezed}")
print(f"New shape: {x_unsqueezed.shape}")
```

    Previous tensor: tensor([1, 2, 3, 4, 5])
    Previous shape: torch.Size([5])
    
    New tensor: tensor([[1, 2, 3, 4, 5]])
    New shape: torch.Size([1, 5])
    
