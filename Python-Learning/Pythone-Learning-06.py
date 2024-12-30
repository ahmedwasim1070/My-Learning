# OOP in python
# To map with real world senarios, we started using abjects in code
# This called object oriented code
# Objects>Function
# Class and Objects in Python
# Class is a blueprint of creating Objects
# Example
# class studnets:
#     name="hamza"
#     name1="ali"
#     name2="ahmed"
#     color="brown"
#     className="ICS"
# get_color=studnets()
# print(get_color.color)
# print(get_color.className)

# Constructor
# init Function
# All classes have a function called_init_(),which is always executed when the class is bieng initiated 
# init function always get executed
# Example
# class student:
#     def __init__(self,name):
#         self.name=name
# s1=student(input("Enter Name : "))
# print(s1.name)
# s2=student("muhammad")
# print(s2.name)

# Practice Question

# 1
# class college:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    # def get_avg(self):
    #     sum=0
    #     for i in self.marks:
    #         sum+=i
    #     print(sum/3)
# s=college("ahmed",[54,46,43])
# print(s.name,s.marks)
# print(s.get_avg())

# Static Method 
# Methods that don't use self parameter
# Example
# class college:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     @staticmethod
#     def hello():
#         print("hello")
#     def get_avg(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         print(sum/3)
    
# s1=college("ahmed",[12,32,12])
# print(s1.name , s1.marks)
# s1.get_avg()
# s1.hello()
        
# Abstraction
# Hiding the implementation details of a class and only showing the essential features to the user.
# Example
# class car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("car started")
# car1=car()
# car1.start()
# Encapsulation
# Wrapping data and fucntions into a single unit (object)
# del keyword 
# Used to del object or propertise or object itself
# del s1.name
# del s1
# Private(like) attributes and methods 



#  Practice Question

# 1
# class Cirle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius**2
#     def para(self):
#         return 2*3.13*self.radius
# c1 = Cirle(12)
# print(c1.radius)
# print(c1.area())
# print(c1.para())

# 2
# class Employe:
#     def __init__(self,role,department,salary):
#         self.role=role
#         self.department=department
#         self.salary=salary
#     def showDetails(self):
#         print(self.role)
#         print(self.department)
#         print(self.salary)
# class Enginer(Employe):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Enginier","IT","75,000")
# e1=Employe("Manager","I-T","10000")
# print(e1.showDetails())
# e2=Enginer("ali","12")
# e2.showDetails()

# 3
# class order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price
#     def __gt__(self,order2):
#         return self.price>order2.price
# order1=order("chips",100)
# order2=order("tea",21)
# print(order1>order2)





