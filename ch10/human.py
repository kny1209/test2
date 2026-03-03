class Human:
    eyes = 2
    nose = 1
    mouth = 1

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("eat")

    def sleep(self):
        print("sleep")

    def talk(self):
        print("talk")

    def intro(self):
        print("name :",self.name,"\nage :",self.age)
    
class Student(Human):
    def __init__(self, name, age, studentnum):
        super().__init__(name,age)
        self.studentnum = studentnum
    
    def study(self):
        print("study")
        
    def intro(self):
        super().intro()
        print("studentnum :",self.studentnum)

lee = Human("leesu",46)
lee.intro()
lee.eat()
lee.sleep()
lee.talk()
print("eyes :",lee.eyes)

print("------------------")

koo = Student("koona",24,202213043)
koo.study()
koo.intro()
print("nose :",koo.nose)

print("------------------")
park = Student("parkwon",31,202210347)
park.intro()
print("mouth :",park.mouth)