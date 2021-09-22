class Ninja:
    def __init__(self, name, age, gender, level, grades=None):
        self.name = name
        self.age = age
        self.gender = gender
        self.level = level
        self.grades = grades or {}

    def setGrade(self, course, grade):
        self.grades[course] = grade

    def getGrade(self, course):
        return self.grades[course]

    def getGPA(self):
        return sum(self.grades.values())/len(self.grades)

naruto = Ninja("naruto", 12, "male", 6, {"NinjaTrain":9.9})
sakura = Ninja("sakura", 12, "female", 6, {"NinjaTrain":6.5})
sasuke = Ninja("sasuke",12,"male",6,{"NinjaTrain":8.3})

print(naruto.getGPA())
print(sakura.getGPA())
print(sasuke.getGrade())