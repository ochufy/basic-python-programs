import random as r
a,b=map(int,input("Enter the limits: ").split())
print('Random number b\w {} and {} -> '.format(a,b),r.randint(a,b))  #or random.randrange(a,b+1)
