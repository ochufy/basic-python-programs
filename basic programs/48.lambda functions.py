func = lambda x:x**2 #returns square of passed value

print(func(5))
print()

def f1(n):
    return lambda a:a*n #returns n*a

f2 = f1(2) #f2 = 2*a
print(f2(5)) #returns 2*5
