class A:
    def inA(obj):
        print("from A")

class B(A):
    def inB(obj):
        print("from B")

obj1 = B()

obj1.inB()

obj1.inA()
