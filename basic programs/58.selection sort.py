lst = list(map(int, input("Enter the numbers: ").split()))

for i in range(len(lst)):
    min = i
    for j in range(i+1, len(lst)):
        if(lst[j]<lst[min]):
            min = j
    lst[i],lst[min] = lst[min],lst[i]

print(lst)
