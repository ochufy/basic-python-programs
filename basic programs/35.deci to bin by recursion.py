def decitobin(n):
    if n>1:
        decitobin(n//2)
    print(n%2,end="")


num=int(input("Enter the decimal number: "))
print(num,"in binary:",end=" ")
decitobin(num)
