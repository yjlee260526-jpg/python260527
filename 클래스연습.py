
# (1) 클래스 정의
class Person:
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))


p1 = Person()
p2 = Person()
p2.name = "이윤주"

p1.print()
p2.print()