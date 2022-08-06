print("1.Kilometers to Miles")
print("2.Mile to Kilometers")
ch=int(input("Enter your choice: "))
v=float(input("Enter the value: "))
if ch==1:
    result=v/1.60934
    print("{} Kilometers = {} Miles".format(v,round(result,2)))
else:
    result=v*1.60934
    print("{} Miles = {} Kilometers".format(v,round(result,2)))
