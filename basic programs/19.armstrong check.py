n=int(input("Enter the number: "))
d=0
m,a=n,n
s=0
while n>=1:
    n/=10
    d+=1
while m>=1:
    r=int(m%10)
    m/=10
    s+=(r**d)
print(s)
if s==a:
    print("It's an Armstrong number")
else:
    print("Not an Armstrong number")
