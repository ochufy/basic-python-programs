def recursum(n):
    if n>=1:
        return n+recursum(n-1)
    else:
        return n


num=int(input("Enter the no. of terms: "))
print("Sum =", recursum(num))
