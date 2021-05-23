"""
class Car:
    def __init__(self, breand, model, year):
        self.breand = breand
        self.model = model
        self.year = year   
        
    def breandmodel(self):
        return f'Araba markası {self.breand} ve modeli {self.model}'

car_1 = Car('BMW', 'i5', 2010)
car_2 = Car('AUDİ', 'x6', 2012)


print(car_1)
print(car_1.breand)
print(car_1.breandmodel())"""


"""

class movie:
    def __init__(self, name, director):
        self.name = name
        self.director = director
        
movie_1 = movie('Full Metal Jacket' , 'Kubrick')
movie_2 = movie('Babel', 'Irarutu')
print(movie_1.director)
print(movie_2.director)
"""
"""
class Student:
    
    scholl_name = 'X high School'
    number_of_students = 0
    
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
        Student.number_of_students += 1
        
    def average(self):
        return sum(self.grades) / len(self.grades)
    
    def schoolName(self):
        return f'My School name {self.scholl_name}'
    
    @classmethod
    def display_school_name(cls, name_of_school):
        cls.scholl_name = name_of_school
        
    @staticmethod
    def statik():
        return f'Only this  message send'
        

    
    
student_1 = Student('Mahmut', 33, [14, 26, 72, 84])
student_2 = Student('Fatma', 25, [20, 40, 70, 90])


print(Student.statik())
print(student_1.statik())
print(student_2.statik())

"""
"""
class Student:
    
    
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
       
        
    def average(self):
        return sum(self.grades) / len(self.grades)
    

student_1 = Student('Mahmut', 33, [14, 26, 72, 84])
student_2 = Student('Fatma', 25, [20, 40, 70, 90])

class Universtystudent(Student):
    def __init__(self, name, age, grades, universty):
        super().__init__(name, age, grades)
        self.universty = universty
        
u_student_1 = Universtystudent('arin', 22, [10, 20, 30], 'ITU')

print(u_student_1.universty)
print(u_student_1.average())"""

"""
class Circle:
    pi = 3.14
    
    def  __init__(self, radius=1):
        self.radius = radius
        
    def area(self):
        return self.radius * self.radius * self.pi
    
    def __repr__(self):
        return f'{__class__.__name__} nesnesi ve yarıçapı {self.radius}'
    
    def __len__(self):
        return self.radius * self.radius

circle_2 = Circle(8)

print(len(circle_2))
print(dir(circle_2))
"""

class Student:
    
    
    def __init__(self, name, surname, age, grades):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades
       
        
    def average(self):
        return sum(self.grades) / len(self.grades)
    
    @property
    def fullname(self):
        return f'{self.name} {self.surname}'
    
student_1 = Student('arin', 'yazilim', 22, [10, 20, 30])

student_1.name='Mahmut'
student_1.surname = 'yazilim_2'
student_1.grades = [50, 50, 50]

print(student_1.name)
print(student_1.surname)
print(student_1.fullname)
print(student_1.average())