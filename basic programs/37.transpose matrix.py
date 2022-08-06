import numpy as np
r,c=map(int,input("Enter the size of matrix: ").split())
values=list(map(int,input("Enter the elements:\n").split()))
matrix=np.array(values).reshape(r,c)
print("Input Matrix:-\n",matrix)
tr=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for r in tr:
    print(r)

'''
print(matrix.T)        
         OR    
print(numpy.transpose(matrix)   
'''