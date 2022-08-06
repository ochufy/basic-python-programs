a,b=map(int,input("Enter two numbers: ").split())
if a>b:
    small=b
else:
    small=a
for i in range(1,small+1):
    if a%i==0 and b%i==0:
        hcf=i
print("HCF =",hcf)

#using gcd() funtion in math module
import math
print("hcf =",math.gcd(a,b))