class Human:
    def __init__(self,name,age,height,gender):
        self.name=name
        self.age=age
        self.height=height
        self.gender=gender

    def displayage(self):
        print(f"i am {self.name} years old")


c1= Human("john",50,1.95,"M")
c2= Human("beri",90,1.83,"F")
c1.displayage()
c2.displayage()
