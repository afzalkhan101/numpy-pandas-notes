#1D array
import numpy as np

arr = np.array([2,2,3],)
print(arr.ndim)
print(arr.shape)
print(arr.size)
print(arr.dtype)

###2d array
arr = np.array([[12,32,33],[22,33,44]])
print("Shape is :",arr.shape)
print("size is :",arr.size)
print("number of Dimentional:",arr.ndim)
print("Number of value is:",arr.size)
print("type of Data:",arr.dtype)


### 3d array
arr = np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])

print(arr.ndim)
print(arr.size)
print(arr.shape)


### Zero D array
arr = np.array(45)
print(arr.size)
print(arr.ndim)
print(arr.shape)
print(arr.dtype)


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)