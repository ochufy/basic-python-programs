import numpy as np
r1,c1=map(int,input("Enter  size of 1st matrix: ").split())
r2,c2=map(int,input("Enter size of 2nd matrix: ").split())
if c1==r2:
    val1=list(map(int,input("Enter elements of 1st matrix:\n").split()))
    mat1=np.array(val1).reshape(r1,c1)
    val2=list(map(int,input("Enter elements of 2nd matrix:\n").split()))
    mat2=np.array(val2).reshape(r2,c2)
    val3=[[0 for x in range(r1)] for y in range(c2)]
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                val3[i][j]+=mat1[i][k]*mat2[k][j]
    prod=np.array(val3).reshape(r1,c2)
    print("Product Matrix:-\n",prod)
else:
    print("Multiplication not possible!")
