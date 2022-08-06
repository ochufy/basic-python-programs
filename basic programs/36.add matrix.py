import numpy
r1=int(input("Enter no. of rows of 1st matrix: "))
c1=int(input("Enter no. of columns of 1st matrix: "))
r2=int(input("Enter no. of rows of 2nd matrix: "))
c2=int(input("Enter no. of columns of 2nd matrix: "))
if r1==r2 and c1==c2:
    mat1=list(map(int,input("Enter elements of matrix 1:\n").split()))
    print(numpy.array(mat1).reshape(r1,c1))
    mat2=list(map(int,input("Enter elements of matrix 2:\n").split()))
    print(numpy.array(mat2).reshape(r1,c1))
    print("Sum Matrix:-")
    mat3=numpy.add(mat1,mat2)
    print(numpy.array(mat3).reshape(r1,c1))
else:
    print("Unable to perform addition!")
