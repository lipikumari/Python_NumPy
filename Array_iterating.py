#Numpy Array Iterating
#Itreating means going through elements one by one.
#Iterating 1-D Arrays
#Example 1
import numpy as np
arr=np.array([1,2,3,4,5])
for x in arr:
    print(x)
#Example 2
import numpy as np
arr=np.array([6,7,8,9,3])
for x in arr:
    print(x)
#Iterating 2-D Arrays
#Example 1
import numpy as np
arr=np.array([[1,2,3,4],[1,8,9,6]])
for x in arr:
    print(x)
#Example 2
import numpy as np
arr=np.array([[6,7,8],[9,4,5]])
for x in arr:
    for y in x:
        print(y)
#Iterating 3-D Arrays
#Example 1
import numpy as np
arr=np.array([[[1,2,3],[7,8,9]],[[8,9,7],[7,0,9]]])
for x in arr:
    print(x)
#Example 2
import numpy as np
arr=np.array([[[2,3,4],[8,9,7]],[[2,3,1],[1,2,3]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)
#Iterating array using nditer()
#Example 1
import numpy as np
arr=np.array([[[1,2],[3,4]],[[3,2],[4,1]]])
for x in np.nditer(arr):
    print(x)
#Example 2
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
for x in np.nditer(arr):
    print(x)
#Iterating arrays with diffrent data types
#we can use 'op_dtypes'argument and pass it the expected to change the datatype of elements while iterating.
#Example 1
import numpy as np
arr=np.array([1,2,3,4])
for x in np.nditer(arr, flags=['buffered'],op_dtypes=['S']):
    print(x)
#Iterating with diffrent size
import numpy as np
arr=np.array([[1,2,3,4],[3,4,5,6]])
for x in np.nditer(arr[: , ::2]):
    print(x)
#Example 2
import numpy as np
arr=np.array([[1,2],[3,4]])
for x in np.nditer(arr[:,::2]):
    print(x)
#Enumerated iteration using 'ndenumerate()'
#Enumeration means mentioning sequence number of somethings one by one
#Example 1  enumerate on 1-D array
import numpy as np
arr=np.array([1,2,3,4])
for idx,x in np.ndenumerate(arr):
    print(idx,x)
#Example 2 enumerate on 2-D array
import numpy as np
arr=np.array([[1,2,3,4],[2,3,4,5]])
for idx,x in np.ndenumerate(arr):
    print(idx,x)

