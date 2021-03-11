#Numpy Array Join
#Joining means putting contents of two or more arrays in a single array.
#Join two arrays
#Example 1
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([3,5,7])
arr=np.concatenate((arr1,arr2))
print(arr)
#Example 2
import numpy as np
arr1=np.array([4,5,6])
arr2=np.array([1,2,3])
arr3=np.array([2,7,9])
arr=np.concatenate([arr1,arr2,arr3])
print(arr)
#joing 2-D arrays
import numpy as np
arr1=np.array([[1,3,6],[3,7,8]])
arr2=np.array([[1,2,3],[2,3,1]])
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)
#Joining arrays using stack function
#Example 1
import numpy as np
arr1=np.array([[1,2,3],[6,7,8]])
arr2=np.array([[2,3,1],[3,4,2]])
arr=np.stack((arr1,arr2), axis=1)
print(arr)
#Example 2
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([3,4,5])
arr=np.stack((arr1,arr2), axis=1)
print(arr)
#Stacking using rows "hstack()"
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([3,4,5])
arr=np.hstack((arr1,arr2))
print(arr)
#Stacking using columns "vstack()"
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([3,4,5])
arr=np.vstack((arr1,arr2))
print(arr)
#stacking along height or depth "dstack()"
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([3,8,9])
arr=np.dstack((arr1 , arr2))
print(arr)
