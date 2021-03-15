#Numpy splitting Array
#We use array_split() for splitting arrays
#Splitting is reverse operation of Joining.
#Example 1
import numpy as np
arr=np.array([1,2,3,4,5,3,4,])
newarr=np.array_split(arr,3)
print(newarr)
#Example 2
import numpy as np
arr=np.array([1,3,2,4,4,56,5])
newarr=np.array_split(arr,4)
print(newarr)
#Split into array
import numpy as np
arr=np.array([1,4,3,2,1,1,22,32,121])
newarr=np.array_split(arr,3)
print(arr[0])
print(arr[1])
print(arr[2])
#splitting 2-D arrays
#Example 1
import numpy as np
arr=np.array([[1,2,3,4],[3,4,5,6],[3,4,5,5]])
newarr=np.array_split(arr,3)
print(newarr)
#Example 2
import numpy as np
arr=np.array([[1,2],[1,2],[3,2],[2,4],[4,5],[5,4],[6,3],[7,8]])
newarr=np.array_split(arr,3,axis=1)
print(newarr)
#example 3
import numpy as np
arr=np.array([[1,2,3],[3,4,5],[3,4,5],[1,4,3],[2,2,1],[2,3,5]])
newarr=np.array_split(arr,3)
print(newarr)
newarr=np.hsplit(arr,3)
print(newarr)

