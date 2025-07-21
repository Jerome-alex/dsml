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
print("transpose of matrix is")
transpose= np.transpose(matrix)
print(transpose)
