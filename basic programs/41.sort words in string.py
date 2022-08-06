s=input("Enter the string: ")
wordlist=s.split()
wordlist.sort()
print("Sorted string:-")
for i in wordlist:
    print(i,end=" ")

'''
wordlist.sort(reverse=True) - sort in descending order
def findlength(w):
    return len(w)
wordlist.sort(key=findlength) - key specifies sorting criteria
'''
