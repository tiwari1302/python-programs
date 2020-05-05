import random


class student:
    name = ""
    roll = 1
    def getName(self):
        self.name = input("Enter the name of the student: ")
    def getRoll(self):
        self.roll = int(input("Enter the roll number of the student: "))
    def showName(self):
        print("Name of student:", self.name)
    def showRoll(self):
        print("Roll number of student:", self.roll)


student1 = student()
student1.getName()
student1.getRoll()
#student1.showName()
#student1.showRoll()


print("Name of student 1:",student1.name)
print("Roll no. of student 1:",student1.roll)
