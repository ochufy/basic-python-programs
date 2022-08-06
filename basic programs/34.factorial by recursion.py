def rectorial(n):
    if n<=1:
        return n
    else:
        return n*rectorial(n-1)

num=int(input("Enter the number: "))
print("Factorial =",rectorial(num))