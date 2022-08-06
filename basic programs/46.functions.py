def info(name, age=20): #default arg age=20
    print('\nName:', name, '\nAge:', age)

nm = input("Enter name: ")
ag = input("Enter age: ")

info(nm)
print()

def lstfunc(lst): #passing list to function
    for i in lst:
        print(i, end=' ')

lstfunc([10,20,30,40])
print()

def findsum(*num): #variable length args
    s=0
    for i in num:
        s+=i
    print(s)

findsum(1,2,3,4,5)
