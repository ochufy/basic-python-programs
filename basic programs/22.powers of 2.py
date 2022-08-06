n=int(input("Enter the limiting power: "))
powers=list(map(lambda x:2**x, range(n)))
for i in range(n):
    print("2 power",i,"is",powers[i])
