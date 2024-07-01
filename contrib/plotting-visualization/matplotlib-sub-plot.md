### 1. Using `plt.subplots()`

The `plt.subplots()` function is a versatile and easy way to create a grid of subplots. It returns a figure and an array of Axes objects.

#### Code Explanation

1. **Import Libraries**:
   ```python
   import matplotlib.pyplot as plt
   import numpy as np
   ```

2. **Generate Sample Data**:
   ```python
   x = np.linspace(0, 10, 100)
   y1 = np.sin(x)
   y2 = np.cos(x)
   y3 = np.tan(x)
   ```

3. **Create Subplots**:
   ```python
   fig, axs = plt.subplots(3, 1, figsize=(8, 12))
   ```

   - `3, 1` indicates a 3-row, 1-column grid.
   - `figsize` specifies the overall size of the figure.

4. **Plot Data**:
   ```python
   axs[0].plot(x, y1, 'r')
   axs[0].set_title('Sine Function')
   
   axs[1].plot(x, y2, 'g')
   axs[1].set_title('Cosine Function')
   
   axs[2].plot(x, y3, 'b')
   axs[2].set_title('Tangent Function')
   ```

5. **Adjust Layout and Show Plot**:
   ```python
   plt.tight_layout()
   plt.show()
   ```

#### Result

The result will be a figure with three vertically stacked subplots.
![subplot Chart](images/subplots.png)

### 2. Using `plt.subplot()`

The `plt.subplot()` function allows you to add a single subplot at a time to a figure.

#### Code Explanation

1. **Import Libraries and Generate Data** (same as above).

2. **Create Figure and Subplots**:
   ```python
   plt.figure(figsize=(8, 12))
   
   plt.subplot(3, 1, 1)
   plt.plot(x, y1, 'r')
   plt.title('Sine Function')
   
   plt.subplot(3, 1, 2)
   plt.plot(x, y2, 'g')
   plt.title('Cosine Function')
   
   plt.subplot(3, 1, 3)
   plt.plot(x, y3, 'b')
   plt.title('Tangent Function')
   ```

3. **Adjust Layout and Show Plot** (same as above).

#### Result

The result will be similar to the first method but created using individual subplot commands.

![subplot Chart](images/subplots.png)

### 3. Using `GridSpec`

`GridSpec` allows for more complex subplot layouts.

#### Code Explanation

1. **Import Libraries and Generate Data** (same as above).

2. **Create Figure and GridSpec**:
   ```python
   from matplotlib.gridspec import GridSpec
   
   fig = plt.figure(figsize=(8, 12))
   gs = GridSpec(3, 1, figure=fig)
   ```

3. **Create Subplots**:
   ```python
   ax1 = fig.add_subplot(gs[0, 0])
   ax1.plot(x, y1, 'r')
   ax1.set_title('Sine Function')
   
   ax2 = fig.add_subplot(gs[1, 0])
   ax2.plot(x, y2, 'g')
   ax2.set_title('Cosine Function')
   
   ax3 = fig.add_subplot(gs[2, 0])
   ax3.plot(x, y3, 'b')
   ax3.set_title('Tangent Function')
   ```

4. **Adjust Layout and Show Plot** (same as above).

#### Result

The result will again be three subplots in a vertical stack, created using the flexible `GridSpec`. 

![subplot Chart](images/subplots.png)

### Summary

- **`plt.subplots()`**: Creates a grid of subplots with shared axes.
- **`plt.subplot()`**: Adds individual subplots in a figure.
- **`GridSpec`**: Allows for complex and custom subplot layouts.

By mastering these techniques, you can create detailed and organized visualizations, enhancing the clarity and comprehension of your data presentations.