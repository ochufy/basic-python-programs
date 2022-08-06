from threading import *
from time import sleep

class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(0.5)

class world(Thread):
    def run(self):
        for i in range(5):
            print("world")
            sleep(0.5)

obj1 = hello()
obj2 = world()

obj1.start()
sleep(0.2)
obj2.start()

obj1.join()
obj2.join()
print("OVER")
