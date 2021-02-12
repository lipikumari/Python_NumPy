#Numpy creating arrays
#Creating a numpy ndarray object
import numpy as np
arr=np.array([6,7,8,9,4])
print(arr)
print(type(arr))
#0-D Array
import numpy as np
arr=np.array(42)
print(arr)
#1-D Array
import numpy as np
arr=np.array([1,3,5,7])
print(arr)
#2-D Array
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr)
#3-D Arrays
import numpy as np
arr=np.array([[1,6,7],[5,8,9],[10,4,8]])
print(arr)
#check number of dimension
import numpy as np
a=np.array(12)
b=np.array([1,5,6])
c=np.array([[1,3,5],[5,7,9]])
d=np.array([[[1,3,5],[3,6,7]],[[3,8,7],[1,5,7]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
#Higher dimensional Array
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
