string=input("Enter the string: ")
newstring=""  #for storing string w/o punctuation
punc='''.,?'"!'''
for i in string:
    if i not in punc:
        newstring += i
print(newstring)
