a,b=map(float,input("Enter the two operands: ").split())
op=input("Enter the operator: ")
if op=='+':
    print("Sum =",a+b)
elif op=='-':
    print("Difference =",a-b)
elif op=='*':
    print("Product -",a*b)
elif op=='/':
    print("Quotient =",round(a/b,2))
else:
    print("Invalid operator!")
