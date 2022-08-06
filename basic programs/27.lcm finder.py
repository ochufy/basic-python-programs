def lcmfinder(a,b):
    big=max(a,b)
    small=min(a,b)
    i=big
    while(True):
       if i%small==0:
           return i
       i+=big

a,b=map(int,input("Enter two numbers: ").split())
print("LCM of",a,"and",b,"is:",lcmfinder(a,b))