#Numpy Array shape
#shape of an array is the number of elements in each dimension.
#Get the shape of an array "shape"
import numpy as np
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)
import numpy as np
arr=np.array([[1,3,5,7],[2,3,4,5],[2,4,5,6]])
print(arr.shape)
#ndmin
import numpy as np
arr=np.array([1,2,3,4], ndmin=5)
print(arr)
print('shape of an array:', arr.shape)
import numpy as np
arr=np.array([2,4,6,8], ndmin=6)
print(arr)
print('shape of an array:',arr.shape)
