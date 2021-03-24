#Numpy Array Searching
#Searching arrays
#we can search the array in numpy using "where()"
#Example 1
import numpy as np
arr=np.array([1,2,3,4,5,6,4])
newarr=np.where(arr==4)
print(newarr)
#Example 2
import numpy as np
arr=np.array([6,7,3,3,8,9,4,5])
x=np.where(arr==3)
print(x)
#Example 3
import numpy as np
arr=np.array([1,2,3,3,4,3,4,5,4,6,3])
x=np.where(arr%2==0)
print(x)
x=np.where(arr%2==1)
print(x)
#search sorted - There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
#The searchsorted() method is assumed to be used on sorted arrays
#Example 1
import numpy as np
arr=np.array([2,6,8,9])
x=np.searchsorted(arr,8)
print(x)
x=np.searchsorted(arr,6)
print(x)
#example 2 search from right side
import numpy as np
arr=np.array([6,7,8,9])
x=np.searchsorted(arr,7,side="right")
print(x)
#Example 3 search from left side
import numpy as np
arr=np.array([2,4,5,6,7])
x=np.searchsorted(arr,4,side="left")
print(x)
#Example 4 Multiple values
import numpy as np
arr=np.array([2,3,4,5,6,7,8,9])
x=np.searchsorted(arr,[2,4,6])
print(x)
