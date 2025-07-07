import numpy as np
rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
data=[]
print("enter the elements")
for i in range(rows):
	row = list(map(int, input(f"Enter row {i + 1} elements: ").split()))
	data.append(row)
matrix=np.array(data)
print("matrix:")
print(matrix)
print("inverse of matrix is")
inverse= np.linalg.inv(matrix)
print(inverse)
