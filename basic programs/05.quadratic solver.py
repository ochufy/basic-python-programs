import cmath
a,b,c=map(int, input("Enter the coefficients of 'a' ,'b' and 'c': ").split())
d=(b**2)-(4*a*c)
if d>0:
    print("real and distinct roots")
    r1=(-b+(d**0.5))/(2*a)
    r2=(-b-(d**0.5))/(2*a)
    print("roots are - %.2f & %.2f" %(r1,r2))
elif d==0:
    print("real and equal roots")
    r1=(-b)/(2*a)
    r2=(-b)/(2*a)
    print("roots are - %.2f & %.2f" %(r1,r2))
else:
    print("imaginary roots")
    r1=(-b+(cmath.sqrt(d)))/(2*a)
    r2=(-b-(cmath.sqrt(d)))/(2*a)
    r1=complex(round(r1.real, 2), round(r1.imag, 2))
    r2=complex(round(r2.real, 2), round(r2.imag, 2))
    print("roots are - ",r1, "and", r2)
