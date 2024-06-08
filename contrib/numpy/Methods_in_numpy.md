# Methods in Numpy
# NumPy insert():

 The insert() method adds the values along the given axis at specified indices.
 
 **syntax** :

    numpy.insert(array, obj, values, axis)
    
**insert() Arguments** :

The insert() method takes four arguments:

* array - original array
* obj - indices at which values are inserted
* values - the array to be inserted at the given position
* axis(optional) - the axis along which the values are inserted

**Example**:

      import numpy as np

      #create an array
  
      numbers = np.array([0, 1, 3, 4])

      #insert 4 at index 2
  
      array2 = np.insert(numbers, 2, 4)

      print(array2)

**Output**:
 
 [0 1 4 3 4]

# NumPy delete():

The delete() method deletes the values at specified indices.

**Syntax**:

   numpy.delete(array, obj, axis = None)

**delete() Arguments** :

The delete() method takes four argument

* array - array to delete elements from
* obj - indices at which values are deleted
* axis(optional) - the axis along which the values are deleted

  **Example**:

        import numpy as np

        array1 = np.array([0, 1, 2, 3])

        # delete at index 2

        array2 = np.delete(array1, 2)

        print(array2)

**Output**:

[0 1 3]
# NumPy append():

The append() method adds the values at the end of a NumPy array.

**Syntax** :

      numpy.append(array, values, axis)

**append() Arguments**:

The append() method takes three arguments:

* array - original array
* values - the array to be appended at the end of the original array
* axis - the axis along which the values are appended

  **Example**:

        import numpy as np
  
        array1 = np.array([1, 2, 3])
  
        array2 = np.array([4, 5, 6])

        # append array2 to array1
  
        array3 = np.append(array1, array2)

        print(array3)

**Output**:

[1 2 3 4 5 6]

# NumPy flip()

The flip() method reverses the order of the elements in an array.

**Syntax** :

    numpy.flip(array, axis = None)

**flip() Arguments**:

The flip() method takes two arguments:

* array - an array with elements to be flipped
* axis(optional) - axis to flip ( None or int or tuple )

**Example**:

       import numpy as np

       # create an array
  
       array1 = np.array([0, 1, 2, 3, 4])

       # flip the elements of array1
  
       array2 = np.flip(array1)

       print(array2)

**Output**:

[4 3 2 1 0]

# NumPy flatten()

The flatten() method flattens a NumPy array without changing its data.

**Syntax**:

     ndarray.flatten(order)

**flatten() Argument**:

The flatten() method takes one argument:

* order (optional) - specifies the order in which the array elements are flattened

**Example**:

      import numpy as np

      # create a two-dimensional array
      
      array1 = np.array([[0, 1], [2, 3]])

      # flatten an array
      
      array2 = array1.flatten()

      print(array2)

**Output**:

[0 1 2 3]
    

      



   

   
