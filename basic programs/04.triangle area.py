a=float(input("Enter first side: "))
b=float(input("Enter second side: "))
c=float(input("Enter third side: "))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area = %.2f" %area)

#conversions
'''print("%o" %(23)) - dec to oct
print(oct(23)) - dec to oct
print(bin(23)) - dec to bin
print(hex(23)) - dec to hex
print("%x" %(23))'''
