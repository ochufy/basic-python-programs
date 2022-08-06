lst = list(map(int, input("Enter the numbers: ").split()))

s = int(input("Enter search element: "))

for i in range(len(lst)):
    if lst[i] == s:
        print(s, "found at position", i+1)
        break
else:
    print("Element not found!")
