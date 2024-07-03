#Mathematical Opearations and Functions on arrays
import numpy as np
a=np.array([12,2,3,123,1])
b=np.array([123,1231,231231,123,123])
print(a)
print(b)
print("b-a= ",np.subtract(b,a))
print("b+a= ",np.add(a,b))
print("For 2d arrays")
c = np.array([[1,2,3,4,5],[2,3,4,5,2]])
d=np.array([[1,2,3,4,5],[2,3,4,5,2]])
print(c)
print(d)

print("add both = " , np.add(c,d))
print("np.power(a,b)",np.power(c,d))

