from numpy import *

ar1 = array([5,4,3,2,1])
print(ar1)
print('Array type:', ar1.dtype)
print()

#2D Array
lst = [1,2,3,4,5,6,7,8,9]
print(array(lst).reshape(3,3)) #3row 3col
print()

#array of 1s
ar2 = ones((3,3), int) #3x3 integer array of 1s
print(ar2)
print()

#operations
ar2 = array([1,2,3,4,5])
sum_arr = ar1 + ar2
print(sum_arr)
print(concatenate([ar1,ar2]))
print()

ar3 = ar2 #shallow copy - changes in ar2/ar3 reflects in ar3/ar2(have same address)
ar3[1] = 6
print(ar2)
print(ar3)
print()

ar4 = ar2.copy() #deep copy - creates an entire new copy of array(have diff. address)
ar4[2] = 7
print(ar2)
print(ar4)
