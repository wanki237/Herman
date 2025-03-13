class Human:
    def __init__(self,name,age,height,gender):
        self.name=name
        self.age=age
        self.height=height
        self.gender=gender
c1= Human("john",50,1.95,"M")
c2= Human("herman",50,1.67,"M")
print(f"My name is {c1.name} and i am {c1.age} old")
print(f"Mey name is {c2.name} and i am {c2.age} old")