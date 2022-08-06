print("1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")
ch=int(input("Enter your choice: "))
v=int(input("Enter the value: "))
if ch==1:
    result=(v*(9/5))+32
    print("{}°C = {}°F".format(v,round(result,2)))
else:
    result=(v-32)*(5/9)
    print("{}°F = {}°C".format(v,round(result,2)))
