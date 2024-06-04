import numpy as np

my_list = [1,2,3,4,5]
arr = np.array([my_list, my_list], int)
print(arr)
print(arr.dtype)
print(arr.shape)
arr2 = arr.reshape(1,10)
print(arr)

print(arr2)

arr3 = np.arange(0,10,2)
print(arr3)

arr_linspace = np.linspace(1,10,50)
print(arr_linspace)

a = 10
b = a
b +=12
print(a,b)