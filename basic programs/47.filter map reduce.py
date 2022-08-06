#filter
def evn(n):
    return n%2==0

lst = [1,2,3,4,5,6,7,8]
even_nos = list(filter(evn, lst)) #checks each item in 'lst' by passing to 'evn' function and makes a
print(even_nos)                   #list with only those numbers which returned 'True'

#list(filter(lambda n:n%2==0, lst)) - using lambda function

#map
lst2 = list(i*i for i in lst)
print(lst2)

lst3 = list(map(lambda x:x*x, lst)) #using map() [map(function, iterable)]
print(lst3)                              #takes each item in even_nos and maps it to it's square

#reduce
from functools import reduce

add = reduce(lambda x,y:x+y, lst) #reduce(function, sequence)
print(add)                        #used to apply a particular function passed in its argument to all
                                   #of the list elements mentioned in the sequence passed along
