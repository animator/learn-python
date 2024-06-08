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

# NumPy empty()

The empty() method creates a new array of given shape and type, without initializing entries.

**Syntax** :

     numpy.empty(shape, dtype = float, order = 'C', like = None)

**empty() Arguments**:

The empty() method takes the following arguments:

* shape - desired new shape of the array (can be integer or tuple of integers)
* dtype (optional) - datatype of the returned array
* order (optional) - specifies the order in which the uninitialized values are filled
* like (optional)- reference object to create arrays that are not NumPy arrays

**Example**:

   import numpy as np

   #create an array of uninitialized values
   array1 = np.empty(5)

   print(array1)

**Output**:

[2.23196843e-316 0.00000000e+000 6.94042595e-310 6.94042589e-310 6.94042589e-310]

# Numpy zeros()

The numpy.zeros() function returns a new array of given shape and type, with zeros. 

**Syntax** :

     numpy.zeros(shape, dtype = None, order = 'C')

**zeros() Arguments**:
* shape :	Defines the shape of the new array, e.g., (2, 3) or 2.	Required
* dtype	:  Specifies the desired data type for the array, e.g., numpy.int8. The default is numpy.float64.	Optional
* order :	Memory layout order: 'C' for row-major (C-style), 'F' for column-major (Fortran-style). Default is 'C'.	Optional

**Example**:

      import numpy as np
      a = (3, 2)
      array = np.zeros(a)
      print(array)

**Output** :

 [[0. 0.]
 [0. 0.]
 [0. 0.]]

 # NumPy ones()

 The ones() method creates a new array of given shape and type, filled with ones.

 **Syntax**:

     numpy.ones(shape, dtype = None, order = 'C')

**ones() Arguments**:

 The ones() method takes three arguments:

* shape - desired new shape of the array (can be integer or tuple of integers)
* dtype (optional) - datatype of the returned array
* order (optional) - specifies the order in which the ones are filled

  **Example**:

      import numpy as np
 
      #create a float array of 1s
  
      array1 = np.ones(5,dtype=int)
  
      print('Integer Array: ',array1)

**Output**:

Integer Array:  [1 1 1 1 1]

# NumPy diag()

The diag() method either creates a new ndarray with the given 1D array as its diagonal elements or it extracts the diagonal from the given ndarray.

**Syntax**:

    numpy.diag(array, k = 0)

**diag() Arguments**:

 The diag() method takes the following arguments:

* array - input array (can be array_like)
* k (optional) - an integer number representing the diagonal to retrieve

 **Example** :

       import numpy as np
       
       array1 = np.arange(1, 4)
       
       mainDiagonal = np.diag(array1)
    
       upperDiagonal = np.diag(array1, k = 1)

       lowerDiagonal = np.diag(array1, k = -1)

       print('Array1:\n',array1)

       print('Array1 as main diagonal elements:\n', mainDiagonal)

       print('Array1 as diagonal elements above main diagonal:\n', upperDiagonal)
 
       print('Array1 as diagonal elements below main diagonal:\n', lowerDiagonal)

**Output** :

Array1:
  
[1 2 3]

Array1 as main diagonal elements:

 [[1 0 0]
 
 [0 2 0]
 
 [0 0 3]]
 
Array1 as diagonal elements above main diagonal:

 [[0 1 0 0]
 
 [0 0 2 0]
 
 [0 0 0 3]
 
 [0 0 0 0]]
 
Array1 as diagonal elements below main diagonal:

 [[0 0 0 0]
 
 [1 0 0 0]

 [0 2 0 0]
 
 [0 0 3 0]]

 # NumPy eye()

 The eye() method creates a 2D array with 1s on the diagonal and 0s elsewhere.

 **Syntax**:

     numpy.eye(N, M = None, k = 0, dtype = float, order = 'C')

**eye() Arguments**:

The eye() method takes the following arguments:

* N- Number of rows in the output (can be int)
* M (optional)- Number of columns in the output (can be int)
* k (optional) - the diagonal in question(can be int)
* dtype (optional) - the datatype of the resultant array
* order (optional) - the memory layout of the array (can be 'C' or 'F')

**Example**:

   import numpy as np
   
   #create a 3x3 array with 1s in diagonal and 0s elsewhere

   array1 = np.eye(3)

   print(array1)

**Output**:

[[1. 0. 0.]

 [0. 1. 0.]
 
 [0. 0. 1.]]


# NumPy roll()

The roll() method shifts the elements of the input arrays a given number of times.


**Syntax**:

     numpy.roll(array, shift, axis)

**roll() Arguments**:

The roll() method takes three arguments:

* array - an array with elements to be rolled
* shift - how many steps the element shifts ( int or tuple )
* axis(optional) - axis to roll/shift ( int or tuple )

**Example**:

     import numpy as np
     
     array1 = np.array([0, 1, 2, 3, 4])
  
     #shift elements of array1 by 3 steps
     
     array2 = np.roll(array1, 3)
  
     print(array2)

**Output**:

[2 3 4 0 1]

# NumPy ceil()

The ceil() function rounds up floating point element(s) in an array to the nearest integer greater than or equal to the array element.

**Syntax**:

      numpy.ceil(array, out = None)

**ceil() Arguments**:

The ceil() function takes following arguments:

* array - the input array
* out (optional) - the output array where the result is stored

**Example**:

       import numpy as np
       
       array1 = np.array([[1.2, 2.7, 3.5],
                      [4.8, 5.1, 6.3],
                      [7.2, 8.5, 9.9]])

       result = np.ceil(array1)

       print("Rounded-up values:")
        
       print(result)

**Output**:

Rounded-up values:

[[ 2.  3.  4.]

 [ 5.  6.  7.]
 
 [ 8.  9. 10.]]  

 # NumPy floor()

 The floor() function rounds down each element in an array to the nearest smallest integer.

 **Syntax**:

        numpy.floor(array, out=None)

 **floor() Arguments**:
 
The floor() function takes following arguments:

* array - the input array whose elements are rounded down to the nearest integer.
* out (optional) - the output array where the result is stored

**Example**:

          import numpy as np

          array1 = np.array([1.9, 2.2, 3.1, 4.3])

          result = np.floor(array1)

          print(result)

**Output**:

[1. 2. 3. 4.]  

# NumPy power()

The power() function is used to raise the elements of an array to a specified power.

**Syntax**:

      numpy.power(base, exponent, out=None)

**power() Arguments**:

The power() function takes one argument:

* base - the input array containing base values
* exponent - the exponent value or array, which can be a scalar or an array of the same shape as base.
* out (optional) - the output array where the result will be stored

**Example**:

         import numpy as np

         base = np.array([2, 3, 4])

         exponent = np.array([2, 3, 4])

         result = np.power(base, exponent)

         print(result)

**Output** :

[  4  27 256]

# Numpy tri()

The numpy.tri() function returns an array with ones at and below the k-th diagonal and zeros elsewhere, where k is the given parameter.

**Syntax**:

       numpy.tri(N, M=None, k=0, dtype=<class 'float'>)

**tri() Arguments**:


* N	  : Number of rows in the array.	int
* M	  : Number of columns in the array. By default, M is taken equal to N.	optional
* k	  : The sub-diagonal at and below which the array is filled. k = 0 is the main diagonal, while k < 0 is below it, and k > 0 is above. The default is 0.	optional
* dtype :	Data type of the returned array. The default is float.

**Example**:

          import numpy as np
          
          np.tri(4, 6, 0, dtype=int)

**Output**:

 array(
 
 [[1, 0, 0, 0, 0, 0],
 
  [1, 1, 0, 0, 0, 0],
        
  [1, 1, 1, 0, 0, 0],

       
  [1, 1, 1, 1, 0, 0]])

  
# Numpy iscomplex()

Returns a bool array, where True if input element is complex.

What is tested is whether the input has a non-zero imaginary part, not if the input type is complex.

**Syntax**:

       numpy.iscomplex(x)

**iscomplex() Arguments**:

 * x  : array_like Input array.

**Example**:

          import numpy as np

          np.iscomplex([1+1j, 1+0j, 4.5, 3, 2, 2j]) 

**Output**:

array([ True, False, False, False, False,  True])

# Numpy isnan()

The numpy.isnan() function tests element-wise whether it is NaN or not and returns the result as a boolean array.

**Syntax**:

         numpy.isnan(array [, out])

**isnan() Arguments**:

* array : [array_like]Input array or object whose elements, we need to test for infinity
* out   : [ndarray, optional]Output array placed with result.
      Its type is preserved and it must be of the right shape to hold the output

**Example**:

         import numpy as np

         arr1 = np.array([1,2,np.nan, np.log(-3)])
          
         print (np.isnan(arr1))

**Output**:

array([False, False,  True,  True])

# Numpy isreal()

Returns a bool array, where True if input element is real.

If element has complex type with zero complex part, the return value for that element is True.

**Syntax**:

         numpy.isreal(x)

**isreal() Arguments**:

* x : array_like Input array.

**Example**:

          import numpy as np

          a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j], dtype=complex)

          np.isreal(a)

**Output**:

array([False,  True,  True,  True,  True, False])


          

          
  
         

          
       


       

          
      
       

   

       
    


 



      



     


     
    

      



   

   
