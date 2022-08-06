class student:

    marks = "0" #class variable

    def __init__(self, name, age): #__init__ is like a constructor
        self.nm = name
        self.age = age
        # print("Name:", self.name)
        # print("Age:", self.age)

    def details(self):
        print("Name:", self.nm)
        print("Age:", self.age)

    @classmethod
    def get_marks(cls):
        return cls.marks

st1 = student("roshan", 18) #it's actually passing 3 args - student(st1, "roshan", 18)
student.details(st1)
print()

st2 = student("rohan", 19)
st2.details()
print()

print(st1.nm)
print(st1.age)
print()

print(st1.get_marks(), st2.get_marks())
student.marks = 100
print(st1.get_marks(), st2.get_marks())

#self parameter is a reference to the current instance of the class, and is used to access
#variables that belong to the class


#It does NOT have to be named self , you can call it whatever you like, but it has to be the
#first parameter of any function in the class
