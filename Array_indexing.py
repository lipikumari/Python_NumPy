#Acess Array elements
import numpy as np
arr=np.array([1,3,5,6,9,3])
print(arr[0])
print(arr[1])
print(arr[4])
print(arr[3]+arr[2])
#Acess 2-D Array
import numpy as np
arr=np.array([[2,4,6,8,9,7],[3,5,7,9,8,7]])
print('2nd element on 1st dim: ', arr[0, 1])
print('5th element on 2nd dim: ', arr[1, 4])
print('3rd element on 1st dim: ', arr[0, 2])
#Acess 3-D Array
import numpy as np
arr=np.array([[[2,7,9],[2,8,9]],[[2,5,7],[6,7,9]]])
print(arr[0,1,2])
#Negative indexing
import numpy as np
arr=np.array([[6,7,8,9,1],[1,2,3,7,8]])
print('Last element from 2nd dim:',arr[1,-1])
