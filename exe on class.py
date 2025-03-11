class student:
    def __init__(self,name,age,grades):
        self.name=name
        self.age=age
        self.grades=grades
        
   # def addgrades(self,grades):
       # self.grades.append(grades)

    def average_grade(self):
        if len(self.grades)==0:
            return 0
        return sum(self.grades)/len(self.grades)

   # def displayaverage_grade(self):
      #  print(self.grades)


class form1student(student):
    def average_grade(self):
        print("hello i'm the new average method for form1studenst only")

studnt = student("ohn",20,[12,23,13])    
s1 = form1student("John",20,[12,23,13])
s2 = form1student("peter",45,[13,16,23])
print(s1.average_grade())
print(studnt.average_grade())


