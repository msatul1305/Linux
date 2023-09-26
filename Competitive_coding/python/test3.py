import numpy as np
import sys
arr1=([[1,4,9,16], [25,39,25,2,3], [1,54,96,236,458]])
arr=np.array(arr1)
arr2=np.array([1,23,4545,3,5,5648])
for array in arr.flat:
    print(array)
print(arr2.argmax(), arr.argsort())
print(arr.ndim,arr.size,arr2.nbytes)
