listofnos=list(map(int,input("Enter the numbers in list: ").split()))
print("User list:",listofnos)
n=int(input("\nEnter the no. to check divisibility: "))
newlist=list(filter(lambda x:x%n==0,listofnos))
print("\nNos. divisible by",n,"in the list are:")
for i in range(len(newlist)):
    print(newlist[i])