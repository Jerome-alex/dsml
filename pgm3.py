import numpy as np
arr1=np.array([1,2,3,4,5])
print("first array")
print(arr1)
arr2=np.array([1,2,3,4,5,6])
print("second array")
print(arr2)
if np.array_equal(arr1,arr2):
	print("true")
else:
	print("false")
