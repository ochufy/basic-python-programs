class outer:
    def outclass(self):
        print("in outer class")

    class inner:
        def inclass(self):
            print("in inner class")

out1 = outer()
out1.outclass()

in1 = outer.inner()
in1.inclass()
