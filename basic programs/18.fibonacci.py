n=int(input("Enter the number of terms (>=2): "))
a,b=0,1
print(a,b,end=" ")
for i in range(3,n+1):
    #c=a+b
    print(a+b,end=" ")
    a,b=b,a+b
