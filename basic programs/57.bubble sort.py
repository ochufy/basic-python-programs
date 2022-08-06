lst = list(map(int, input("Enter the numbers: ").split()))

for i in range(len(lst)):
    for j in range(len(lst)-1-i):
        if(lst[j]>lst[j+1]):
            lst[j],lst[j+1] = lst[j+1],lst[j]

print(lst)
