string=input("Enter the string: ").casefold()   #casefold() for caseless comparison
st=string[::-1]   #for reversing the string
if st==string:
    print("It's a palindrome!")
else:
    print("It's not a palindrome")

'''
newstring=reversed(string)
if list(string)==list(newstring):
    print("It's a palindrome!")
'''
