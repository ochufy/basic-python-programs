a,b,c=map(int,input("Enter three numbers: ").split())
if a>=b and a>=c:
    print(a, " is the largest")
elif b>=a and b>=c:
    print(b, " is the largest")
else:
    print(c, " is the largest")