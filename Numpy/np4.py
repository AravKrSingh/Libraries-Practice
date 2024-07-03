import numpy as np
#SORT, FILTER AND SEARCH
ar = np.array([1,2,3,4,5,6,23,12312,213,2,3,4,2,1,34,123,32])
print(np.sort(ar))
ar1=np.sort(ar)
#SEARCHING AN ELEMENT IN AN ARRAY
s=np.where(ar==23)
print("23 exists at index number ",s)
#SEARCH SORTED : FOR THIS ARRAY MUST BE SORTED BEFORE HAND
ss=np.searchsorted(ar1,12312)
print(ss)
print()
print()
#Filter():NEW ARRAY FROM OLD ARRAY
ar2=np.array([1,2,3,4])
tf1=np.array([True,False,True,False])
f=ar2[tf1]
print(f)
#filter with conditions
tf2=ar2>2
new=ar2[tf2]
print(new)
