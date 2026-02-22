import numpy as np

arr1 = np.array([1, 2, 3])
print(arr1)
print(arr1.ndim)
print(arr1.shape)
print("two dimension array")
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(arr2.ndim)
print(arr2[0, 2])
print(arr2[1, -3])

print("three dimension array")

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)
print(arr3.ndim)
print(arr3[0, 1, 2])
print(arr3.shape)

print("one dimension")
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr.size)
print(arr[1:5])
print(arr[4:])

print("string datatypes")

arr_str = np.array(['apple', 'banana', 'orange'])
print(arr_str)
print(arr_str.dtype)

print("Copyyyyyyyyyyyyy and Viewwwwwwwwwwwwww")

arr_copy = np.array([1, 2, 3, 4, 5])
x = arr_copy.copy()
x[0] = 22
print(arr_copy)
print(x)

arr_view = np.array([6, 7, 8, 9])
print(arr_view)
y = arr_view.view()
y[1] = 77
print(arr_view)
print(y)

print("shape of array")

arr_shape = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr_shape.shape)

arr_reshape = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr_reshape)
newarr = arr_reshape.reshape(4, 3)
print(newarr.ndim)
print(newarr)

new_arr = arr_reshape.reshape(2, 3, 2)
print(new_arr)

print("iterating over array")

arr_itr1 = np.array([1, 2, 3, 66, 77])

for i in arr_itr1:
    print(i)

arr_itr2 = np.array([[1, 2, 3], [4, 5, 6]])

for i in arr_itr2:
    print(i)

for x in arr_itr2:
    for y in x:
        print(y)

print("iterater using  nditer")

arr_nditr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr_nditr):
    print(x)

for x in np.nditer(arr_nditr, flags=['buffered'], op_dtypes=['S']):
    print(x)

print("array join")

arr_j1 = np.array([[1, 2], [3, 4]])

arr_j2 = np.array([[5, 6], [7, 8]])

arr_j3 = np.concatenate((arr_j1, arr_j2), axis=1)
print(arr_j3)
arr_j4 = np.concatenate((arr_j1, arr_j2))
print(arr_j4)

print("search array")
arr_search = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr_search == 4)
print(x)
y = np.where(arr_search % 2 == 0)
print(y)

z = np.searchsorted(arr_search, 4)
print(z)
