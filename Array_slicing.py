#Numpy Array Slicing
#Slicing in python means taking elements from one given index to another given index [start:end:step] .
#slicing arrays
#Example 1
import numpy as np
arr=np.array([1,3,8,9,7])
print(arr[1:3])
print(arr[1:5:2])
#Example 2
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
print(arr[3:])
print(arr[:3])
#Negative slicing
print(arr[-5:-1])
print(arr[1:7:2])
print(arr[::3])
#slicing 2-D Arrays
#Example 1
import numpy as np
arr=np.array([[1,2,3,4,5],[6,7,8,9,3]])
print(arr[1,1:4])
print(arr[0:2,2])
print(arr[0:2,1:4])
