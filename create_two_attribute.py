#Create a "Person" class

#that has a name("name") and a age("age")
class Person:
    def __init__(self,name_,age):
        self.name_ = name_
        self.age = age
        
p1 = Person('Ali',25)

print(f"ismi {p1.name_}, yoshi {p1.age}")