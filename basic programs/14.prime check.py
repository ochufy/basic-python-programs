n=int(input("Enter the number: "))
if n==0 or n==1:
    print("neither prime nor composite")
    exit()
for i in range(2,n):
    if n%i==0:
        print("composite number")
        break
else:
    print("prime number")
