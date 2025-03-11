class student:
    def __init__(self,name,department,matricule,courses):
        self.name=name
        self.department=department
        self.matricule=matricule
        self.courses=[]

    def displaystudent(self):
        print(f"My name is {self.name} from the {self.department} department, My matricule is {self.matricule}")
    def addcourses(self,courses):
        self.courses.append(courses)
    def displaycourses(self):
        print(self.courses)
 
               
               
c1 = student("john","computer","UBa24Ph007","maths")  
c1.displaystudent()
c1.addcourses("English")
c1.displaycourses()
c1.addcourses("maths")
c1.displaycourses()
c1.addcourses("French")




c1.displaycourses()

c1.courses.pop(-1)
c1.displaycourses()

      