- The list data structure of python is very highly efficient and is capable of performing various functions. 
- But, they have severe limitations when it comes to the computation of vectorized operations which deals with 
- element-wise multiplication and addition. 
- The python lists also require the information regarding the type of every element 
- which results in overhead as type dispatching code gets executes every time any operation is performed on any element.
- This is where the NumPy arrays come into the picture as all the limitations of python lists are handled in NumPy arrays.
- Additionally, as the size of the NumPy arrays increases, NumPy becomes around 30x times faster than the Python List. 
- This is because the Numpy arrays are densely packed in the memory due to their homogenous nature. 
- This ensures the memory free up is also faster.
- 1-D array:
  - import numpy as np
    one_dimensional_list = [1,2,4]
    one_dimensional_arr = np.array(one_dimensional_list)
    print("1D array is : ",one_dimensional_arr) 
- 2D array creation:
  - import numpy as np
    two_dimensional_list=[[1,2,3],[4,5,6]]
    two_dimensional_arr = np.array(two_dimensional_list)
    print("2D array is : ",two_dimensional_arr)
- 3D array:
  - import numpy as np
    three_dimensional_list=[[[1,2,3],[4,5,6],[7,8,9]]]
    three_dimensional_arr = np.array(three_dimensional_list)
    print("3D array is : ",three_dimensional_arr) 
- ND array creation
  - import numpy as np
    ndArray = np.array([1, 2, 3, 4], ndmin=6)
    print(ndArray)
    print('Dimensions of array:', ndArray.ndim)
- delete the second column and replace the column with a new column value
  - Given array: [[35 53 63]
    [72 12 22]
    [43 84 56]]
  - New Column values:[  
    20
    30
    40
    ]
  - import numpy as np
    #inputs
    inputArray = np.array([[35,53,63],[72,12,22],[43,84,56]])
    new_col = np.array([[20,30,40]])
    # delete 2nd column
    arr = np.delete(inputArray , 1, axis = 1)
    #insert new_col to array
    arr = np.insert(arr , 1, new_col, axis = 1)
    print (arr) 
- efficiently load data from a text file?
  - numpy.loadtxt()
  - file formats that are supported:
    - Text files
    - Raw binary
    - Pickle
    - HDF5
    - npy
- read CSV data into an array in NumPy
  - from numpy import genfromtxt
    csv_data = genfromtxt('sample_file.csv', delimiter=',')
- sort the array based on the Nth column?
  - arr = np.array([[8, 3, 2],
    [3, 6, 5],
    [6, 1, 4]])
  - output: [[6, 1, 4],
    [8, 3, 2],
    [3, 6, 5]]
  - import numpy as np
    arr = np.array([[8, 3, 2],
    [3, 6, 5],
    [6, 1, 4]])
    #sort the array using np.sort
    arr = np.sort(arr.view('i8,i8,i8'),
    order=['f1'],
    axis=0).view(np.int)
- find the nearest value in a given numpy array?
  - import numpy as np
    def find_nearest_value(arr, value):
    arr = np.asarray(arr)
    idx = (np.abs(arr - value)).argmin()
    return arr[idx]
    #Driver code
    arr = np.array([ 0.21169,  0.61391, 0.6341, 0.0131, 0.16541,  0.5645,  0.5742])
    value = 0.52
    print(find_nearest_value(arr, value)) # Prints 0.5645
- reverse the numpy array using one line of code?
  - reversed_array = arr[::-1]
- find the shape of any given NumPy array?
  - import numpy as np
    arr_two_dim = np.array([("x1","x2", "x3","x4"),
    ("x5","x6", "x7","x8" )])
    arr_one_dim = np.array([3,2,4,5,6])
    # find and print shape
    print("2-D Array Shape: ", arr_two_dim.shape)
    print("1-D Array Shape: ", arr_one_dim.shape)
    """
    Output:
    2-D Array Shape:  (2, 4)
    1-D Array Shape:  (5,)
    """
