f1 = open("readfile.txt", "r") #r/w/a - read/write/append
print(f1.read())
f1.close()

f1 = open("readfile.txt", "r")
f2 = open("writefile.txt", "w")
for data in f1:
    f2.write(data)
