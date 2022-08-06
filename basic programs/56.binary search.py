lst = list(map(int, input("Enter the numbers: ").split()))

s = int(input("Enter search element: "))

f = 0
l = len(lst)-1

for i in range(len(lst)):
    mid = (f+l)//2
    if s == lst[mid]:
        print(s, "found at position", mid+1)
        break
    elif s > lst[mid]:
        f = mid+1
    else:
        l = mid-1
else:
    print("Element not found!")
