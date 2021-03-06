#Numpy array copy vs view
#The main diffrence between a copy and a view of an array is that the copy is a new array, and the view is just a view of original array.
#copy
#Example 1
import numpy as np
arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=45
print(arr)
print(x)
#example 2
import numpy as np
arr=np.array([1,3,4,5,6])
x=arr.copy()
arr[1]=2
print(arr)
print(x)

#view
#Example 1
import numpy as np
arr=np.array([1,3,5,7,9])
x=arr.view()
arr[1]=2
print(arr)
print(x)
#example 2
import numpy as np
arr=np.array([1,3,4,7,8,8])
x=arr.view()
arr[5]=9
print(arr)
print(x)
#make changes in its view
import numpy as np
arr=np.array([2,4,6,8,9])
x=arr.view()
x[4]=10
print(arr)
print(x)
import numpy as np
arr=np.array([2,2,3,4,5,6])
x=arr.view()
x[0]=1
print(arr)
print(x)
#Check if array owns its Data
# Every numpy array has attribute "base" that return "none" if the array its own data . otherwise "base"refers to original object.
import numpy as np
arr= np.array([1,2,3,4,5])
x=arr.copy()
y=arr.view()
print(x)
print(y)
print(x.base)
print(y.base)
