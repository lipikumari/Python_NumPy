#Numpy array Reshape
#Reshaping means changing the shape of an array
#Reshape from 1-D to 2-D
#Example 1
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(4,3)
print(newarr)
#Example 2
import numpy as np
arr=np.array([1,2,3,4,5,6])
newarr=arr.reshape(2,3)
print(newarr)
#Reshape from 1-D to 3-D
#Example 1
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr=arr.reshape(2,3,2)
print(newarr)
#returns copy or view?
import numpy as np
arr=np.array([1,5,6,7,8,9,0,8])
print(arr.reshape(2,4).base)
#so its view
#unknown dimension
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8])
newarr=arr.reshape(2,2,-1)
print(newarr)
#flattening the array - Flattening array means converting a multidimensional array into a 1D array.
#We can use reshape(-1) to do this.
#Example 1
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
newarr=arr.reshape(-1)
print(newarr)
#Example 2
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
newarr=arr.reshape(-1)
print(newarr)
