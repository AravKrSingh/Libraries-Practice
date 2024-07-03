import numpy as np
#Arrays are not builtin in Python they are needed to called through Numpy functions
#Declaration of arraay
a=np.array([123,1212,312,312,31])
b=np.array([123,1213,231,23,123])
print(a+b)
print(a*b)
print()
print()
print()
print("product of multielements arryas with single element arrays")
c=np.array([0])
print(a*c)
#We can directlu use mathematical operations on arrays bt we cant do same for lists.And arrays consume less data than list
#CREATING , SLICING AND ATTRIBUTES OF ARRAYS

#MAKING MATRICES USING ARRAYS
d=np.array([[1,2,3,4,5],[12,3,4,21,1],[112,12,3,12,3],[123,123,1231,231,32]])
print(d)
#For making matrix all must have number of elements
print()
print()
print()
print()
#Slicing of ARRAYS
arr=np.array([10,20,30,40,50])
print(arr[:3])
#slicing of nested lists
arr1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr1)
print("SLICING OF ARRAYS : arr1[0:2,0:2]")
print(arr1[0:2,0:2])
print("Slicing of nested arrys[nested arrays index no , slicing] = arr1[1,0:2]")
print(arr1[1,0:2])
print()
print()
print()
print("USING ATTRIBUTES IN ARRAYS")
print("shape")
print(np.shape(arr1))
print("np.size(arr1)")
print(np.size(arr1))
print("No. of dimensions ndim")
print(np.ndim(arr1))
print("dataype")
print(arr1.dtype)
print("length")
print(len(arr1))
print("Change the datatype")
arr1.astype(float)
print(arr1.dtype)
