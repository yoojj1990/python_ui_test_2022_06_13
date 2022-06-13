class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def showName(self):
        print("이름")

class Parent:
    def work(self):
        print("일을 하신다")

class Child(Parent):
    def play(self):
        print("놀기")

worker1 = Parent()
worker1.work()

child1 = Child()
child1.play()
child1.work()

stu1 = Student(10, "홍길동")
stu2 = Student(20, "이순신")

stu1.name
stu1.showName()

