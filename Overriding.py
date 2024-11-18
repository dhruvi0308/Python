class Animal(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

class People(Animal): 
    def __init__(self, age, name, height):
        super().__init__(age, name) 
        self.height = height

    def speak(self):
        print("Hello")

class Student(People):
    def __init__(self, age, name, height, student_id):
        super().__init__(age, name, height)
        self.student_id = student_id
    
    def do_homework(self):
        print(f"Student {self.name} is doing homework")

s = Student(20, "Alex", 60, 12345)
print(s.age, s.name)  
print(s.get_age())
s.speak()
s.do_homework()