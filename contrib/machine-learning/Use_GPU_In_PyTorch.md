# Running tensors on GPUs (and making faster computations)

Deep learning algorithms require a lot of numerical operations.

And by default these operations are often done on a CPU (computer processing unit).

However, there's another common piece of hardware called a GPU (graphics processing unit), which is often much faster at performing the specific types of operations neural networks need (matrix multiplications) than CPUs.

## 1. Getting a GPU

There are three ways to access a GPU:

* Google Colab
* Use your own (local machine)
* Cloud Computing (AWS , Azure)

For now i prefere to use `Google Colab` because it is easy to use.
You can use it from here https://colab.research.google.com/

To check if you've got access to a Nvidia GPU, you can run `!nvidia-smi` where the ! (also called bang) means "run this on the command line".


```python
!nvidia-smi

output -> /bin/bash: line 1: nvidia-smi: command not found
```    

As you can see that it  is showing that  `command not found error` it means currently we do'nt have colab GPU access.

To access the colab GPU follow the below steps:

1. Click on `Runtime` from the above menu.
2. Click on `Change Runtime type`.
3. Currently it is on CPU so click on `T4 GPU` and hit save button.
4. It takes some seconds to connect to the GPU.

Now to check again run the command


```python
!nvidia-smi

output -> Fri May 31 04:01:18 2024       
    +---------------------------------------------------------------------------------------+
    | NVIDIA-SMI 535.104.05             Driver Version: 535.104.05   CUDA Version: 12.2     |
    |-----------------------------------------+----------------------+----------------------+
    | GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
    |                                         |                      |               MIG M. |
    |=========================================+======================+======================|
    |   0  Tesla T4                       Off | 00000000:00:04.0 Off |                    0 |
    | N/A   36C    P8               9W /  70W |      0MiB / 15360MiB |      0%      Default |
    |                                         |                      |                  N/A |
    +-----------------------------------------+----------------------+----------------------+
                                                                                             
    +---------------------------------------------------------------------------------------+
    | Processes:                                                                            |
    |  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
    |        ID   ID                                                             Usage      |
    |=======================================================================================|
    |  No running processes found                                                           |
    +---------------------------------------------------------------------------------------+
 ```   

Whoo!!! now we have GPU access

## 2. Getting PyTorch to run on the GPU

Now we have GPU access! it's time to run tensors on the GPU for faster computation.

To do so, you can use the `torch.cuda` package.

Rather than talk about it, let's try it out.

You can test if PyTorch has access to a GPU using `torch.cuda.is_available()`.


```python
# Check for GPU
import torch
torch.cuda.is_available()

output -> True
```


If the above outputs `True`, PyTorch can see and use the GPU, if it outputs `False`, it can't see the GPU and in that case, you'll have to go back through the installation steps.

Now, let's say you wanted to setup your code so it ran on CPU or the GPU if it was available.

That way, if you or someone decides to run your code, it'll work regardless of the computing device they're using.

Let's create a device variable to store what kind of device is available.


```python
device = "cuda" if torch.cuda.is_available else "cpu"
device

output -> 'cuda'
```



If the above output "cuda" it means we can set all of our PyTorch code to use the available CUDA device (a GPU) and if it output "cpu", our PyTorch code will stick with the CPU.

You can count the number of GPUs PyTorch has access to using `torch.cuda.device_count()`.


```python
torch.cuda.device_count()

output -> 1
```


## 3. Putting tensors on the GPU


```python
# Create a tensor
tensor = torch.tensor([1,2,3])

print(f"Tensor is running on the :{tensor.device}")

output -> Tensor is running on the :cpu
```    

Note: By default tensors run on the 'CPU'


```python
# Move tensor to GPU (if available)
tensor_on_gpu = tensor.to(device)

print(f"Tensor is running on:{tensor_on_gpu.device}")

output -> Tensor is running on:cuda:0
```    

Notice the second tensor has device=`'cuda:0'`, this means it's stored on the 0th GPU available (GPUs are 0 indexed, if two GPUs were available, they'd be `'cuda:0'` and `'cuda:1'` respectively, up to `'cuda:n'`).

## 4. Moving tensors back to the CPU

What if we wanted to move the tensor back to CPU?

For example, you'll want to do this if you want to interact with your tensors with NumPy (NumPy does not leverage the GPU).

Let's try using the `torch.Tensor.numpy()` method on our `tensor_on_gpu`.


```python
# If tensor is on GPU, can't transform it to NumPy (this will error)
tensor_on_gpu.numpy()

output -> 


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-53175578f49e> in <cell line: 2>()
          1 # If tensor is on GPU, can't transform it to NumPy (this will error)
    ----> 2 tensor_on_gpu.numpy()
    

    TypeError: can't convert cuda:0 device type tensor to numpy. Use Tensor.cpu() to copy the tensor to host memory first.

```
Instead, to get a tensor back to CPU and usable with NumPy we can use Tensor.cpu().

This copies the tensor to CPU memory so it's usable with CPUs


```python
# Instead, copy the tensor back to cpu
tensor_back_on_cpu = tensor_on_gpu.cpu().numpy()
tensor_back_on_cpu

output -> array([1, 2, 3])
```

