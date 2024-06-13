# Aggregation in PyTorch

*Aggregation in PyTorch refers to the process of combining multiple values into a single value using operations like sum, mean, or max.*

So let's create a tensor and find the max , min , mean and sum of it.


```python
# First import torch
import torch
print(torch.__version__)

output -> 2.3.0+cu121
```    


```python
# Create a tensor
t = torch.arange(0,100,10)
t

output -> tensor([ 0, 10, 20, 30, 40, 50, 60, 70, 80, 90])
```


* To find `minimum` value in the tensor -> `.min()`
* To find `maximum` value in the tensor -> `.max()`
* To find `mean` of the values in the tensor -> `.mean()`
* To find `sum` of the values in the tensor -> `.sum()`

Now let's perform some aggregation.


```python
print(f" Minumum is :{t.min()}")
print(f"Maximum is :{t.max()}")
print(f"Mean is : {t.type(torch.float32).mean()}")
print(f"Sum is :{t.sum()}")

output -> Minumum is :0
          Maximum is :90
          Mean is : 45.0
          Sum is :450
```    

#### Note:
For `mean` input data must be of `float` or `long` type . So i convert it into float 32 otherwise it will `show error`.

You can also do the same as above with `torch` methods.!!!


```python
torch.max(t), torch.min(t), torch.mean(t.type(torch.float32)), torch.sum(t)

output ->  (tensor(90), tensor(0), tensor(45.), tensor(450))
```


## Positional min/max

You can also find the index of a tensor where the max or minimum occurs with `torch.argmax()` and `torch.argmin()` respectively.


```python
# Returns index of max and min values
print(f"Index where max value occurs: {t.argmax()}")
print(f"Index where min value occurs: {t.argmin()}")

output ->  Index where max value occurs: 9
           Index where min value occurs: 0
```    
