set1=set()
set2=set()
n=int(input("Enter no. of elements(set 1): "))
print("Enter elements:")
for i in range(n):
    set1.add(input())
m=int(input("Enter no. of elements(set 2): "))
print("Enter elements:")
for i in range(m):
    set2.add(input())
#set operations
print("Union -",set1|set2)
print("Intersection -",set1&set2)
print("Set Difference -",set1-set2)
print("Symmetric Difference -",set1^set2)
