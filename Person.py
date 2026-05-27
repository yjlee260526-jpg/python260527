# Person.py - 상속 구조 구현

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}")


class Manager(Person):
    def __init__(self, id, name, title):
        super().__init__(id, name)
        self.title = title
    
    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")


class Employee(Person):
    def __init__(self, id, name, skill):
        super().__init__(id, name)
        self.skill = skill
    
    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")


# 10개의 인스턴스 생성 및 사용
print("=== 10개의 인스턴스 ===\n")

# Person 인스턴스 3개
p1 = Person(1, "김철수")
p2 = Person(2, "이영희")
p3 = Person(3, "박민준")

# Manager 인스턴스 3개
m1 = Manager(101, "이사장", "Director")
m2 = Manager(102, "과장", "Manager")
m3 = Manager(103, "팀장", "Team Lead")

# Employee 인스턴스 4개
e1 = Employee(201, "개발자1", "Python")
e2 = Employee(202, "개발자2", "Java")
e3 = Employee(203, "디자이너", "UI/UX")
e4 = Employee(204, "QA엔지니어", "Testing")

# 모든 인스턴스의 정보 출력
print("--- Person 정보 ---")
p1.printInfo()
print()
p2.printInfo()
print()
p3.printInfo()
print()

print("--- Manager 정보 ---")
m1.printInfo()
print()
m2.printInfo()
print()
m3.printInfo()
print()

print("--- Employee 정보 ---")
e1.printInfo()
print()
e2.printInfo()
print()
e3.printInfo()
print()
e4.printInfo()
