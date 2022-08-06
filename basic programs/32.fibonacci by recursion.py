def fibo(i):
    if i<=1:
        return i
    else:
        return(fibo(i-1)+fibo(i-2))
n=int(input("Enter no. of terms: "))
for i in range(n):
    print(fibo(i),end=' ')
