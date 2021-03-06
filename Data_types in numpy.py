#Data types in Numpy
#Checking data type of an array
#The numpy array object has a property called dtype that returns data type of an array:
import numpy as np
arr=np.array([2,4,6,8])
print(arr.dtype)
import numpy as np
arr=np.array(["Lipi","Kumari","class"])
print(arr.dtype)
#Creating array with defined data type
import numpy as np
arr=np.array([1,2,3,4], dtype='S')
print(arr)
print(arr.dtype)

import numpy as np
arr=np.array([1,3,5,6],dtype='i4')
print(arr)
print(arr.dtype)
#converting data type on existing arrays
import numpy as np
arr=np.array([1.1,2.1,3.1])
newarr= arr.astype('i')
print(newarr)
print(newarr.dtype)
#change data type from integer to boolean
import numpy as np
arr=np.array([1,0,3])
newarr=arr.astype('bool')
print(newarr)
print(newarr.dtype)
