from array import *

ar = array('i', [5,4,3,2,1]) # 'i' for signed int

#print using for-loop
for i in ar:
    print(i, end=" ")

#copying values into another array
ar2 = array(ar.typecode, (2*i for i in ar)) #copy each value in 'ar' multiplied by 2
print()
print(ar2)

#print using while-loop
i = 0
while i<len(ar2):
    print(ar2[i], end=" ")
    i+=1

#user input
ar3 = array('i', []) #empty array
n = int(input("\nEnter size of array: "))
print("Enter values:")
for i in range(n):
    x = int(input())
    ar3.append(x)
print(ar3)
