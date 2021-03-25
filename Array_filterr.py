#Numpy Array filter
#Getting some elements out of an existing array and creating a new array out of them is called filtering.
#we can filter array using boolean index list.
#If true then that element is contained in filter array and if false then excluded from filtered array
#Array filter
#Example 1
import numpy as np
arr=np.array([41,42,43,44])
x=[True , False , True , False]
newarr=arr[x]
print(newarr)
#Example 2
import numpy as np
arr=np.array([2,3,4,5,6,7,8,8])
x=[True , False,True, False,True,True,False,True]
newarr=arr[x]
print(newarr)
#creating the filter array
#Example 1
import numpy as np
arr=np.array([23,3,4,2])
#create an empty list
filter_arr=[]
#go through each element in arr
for element in arr:
    #if the element is higher than 23 , set the value to true,otherwise false:
    if element>23:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)
#Example 2
import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,12,24])
#create an empty list
filter_arr=[]
#go through each element in arr
for element in arr:
    #if the element is divide by 2 , set the value true,otherwise false
    if element%2==0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)
#Creating filter directly from array
#Example 1
import numpy as np
arr=np.array([24,28,36,72])
filter_arr=arr>28
newarr=arr[filter_arr]
print(filter_arr)
print(newarr)
#Example 2
import numpy as np
arr=np.array([2,24,26,28,27,30,29,31,32])
filter_arr=arr%2==0
newarr=arr[filter_arr]
print(newarr)

