s=input("Enter the string: ").casefold()
vowels="aeiou"
count=0
for i in s:
    if i in vowels:
        count+=1
print("Total vowel count -",count)
new={}.fromkeys(vowels,0)  #a dictionary with each vowel count as '0'
for i in s:
    if i in new:
        new[i]+=1
print("Count of each vowel:")
for x,y in new.items():
    print(x,"-",y)
