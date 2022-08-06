a,b=map(int,input("Enter the limits: ").split())
for i in range(a,b+1):
    d=len(str(i))
    s=0
    m=i
    while m>0:
        r=m%10
        s+=(r**d)
        m//=10
    if s==i:
         print(i)
