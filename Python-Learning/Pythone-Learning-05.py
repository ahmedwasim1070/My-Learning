# Function 
# Block of statments that performa a specifi task.
# Example
# def math_cal():
#     a=12
#     b=12
#     sum=a+b
#     print(sum)
# math_cal()
# Example
# def get_number(a,b):
#     sum=a*b
#     print(sum)
# get_number(5,5)
# get_number(5,15)
# get_number(25,5)
# Or
# def cal_num(a,b):
#     return a*b
# sum=cal_num(12,12)
# print(type(sum),sum)
# The function that did not return anything will give none
# Example
# Finding The average of 3 numbers
# def cal_num(a,b,c):
#     return (a+b+c)/3
# avg=cal_num(2,3,4)
# print(avg)
# The return function give some value while calling the function with varaible without it gives null value!
# There are two types of Function
# Built In Fucntion
# Example
# len()
# print()
# type()
# range()
# User Defined Function
# These function are created by the user and can perform different task according to the requirments of the user 
# Practice Question

# 1
# def chk_len(a):
#     return len(a)
# print(chk_len("Hello!"))

# or

# city_list=["karachi","faislabad","multan","lahore","Islamabad"]
# def chk_len(a):
#     return len(city_list[a])
# print(chk_len(3))

# 2
# city_list=["karachi","faislabad","multan","lahore","Islamabad"]
# def list_maker():
#     for i in city_list:
#         print(i,end="")
# list_maker()

# 3
# n=int(input("Enter the Number you want to find Factorial:"))
# def fnd_fact():
#     sum=1
#     for i in range(1,n+1):
#         sum*=i
#     return sum
# print(fnd_fact())

# 4
# n=int(input("enter currency in dollar:"))
# def cnvt_curncy(a):
#     get_n=n*a
#     print(get_n)
# cnvt_curncy(278)

# 5
# n=int(input("Enter the Number:"))
# def chk_n():
#     if(n%2==0):
#         print(n,"is even")
#     else:
#         print(n,"is odd")
# chk_n()

# Recursion
# When a fucntion calls itself repeatedly
# Example
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)
# we use if condiotion to stop the loop of calling the function itself called recursion
# and return returns the control of the program 
# Call stack
# calling the function on the fuction is called call stack
# Imagine the call stack as a bucket call stack will be add the first called function in the base as a first book where we place another book which is other function this will countine to happen until it is stopped by the  condition if not it will keep runing infinitly
# Return refers to returning the variable value back to its previous one and so on and deleting the previous one 
# The condition statment in recurstion is called base case
# Exampe 2 Findin factorial with Recursion
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(int(input("enter the number:"))))

# factorial(11)=n*factorial(11-1)
# factorial(10)=n*factorial(10-1)
# .
# ..
# .
# .
# .
# factorial(2)=n*factorial(2-1)
# factorial(1) if condition true

# Practice Question

# 1
# def get_num(n):
#     if(n==0 or n==1):
#         print(1)
#         return 1
#     get_num(n-1)
#     print(n)

# get_num(8)

# or Profesional way using gpt
# def get_num(n):
#     if (n==0):
#         return 0
#     return get_num(n-1)+n
# print(get_num(5))

# 2
# list=[1,2,3,4,5,6,7,8]
# def get_list(n): 
#     if(n==0):
#         print(list[0])
#         return 0
#     get_list(n-1)
#     print(list[n])
# get_list(len(list)-1)

# or
# num=[1,2,3,4,5,6,7,8]
# def get_list(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     get_list(list ,idx+1)
# get_list(num)


# File I/O in Python
# Open read and close file
# Open
# Example
# open("file_name","character")
# file name is the name of the file along with its path
# character tell what we are going to do with file Example r is used for read w for write 
# r = read 
# w = write and delete the existing data
# x = creating a new file and open it for writing 
# a = "open for writing, appending to the end of the file if it exists"
# b = "binary mode "
# t = "text mode ( default )"
# + = "open a disk file for updatng ( reading and writing )"
# r+ = " use  to read and write it will overwrite the file from the begening and pointer is on the start of the page"
# w+ = " read and overwrite similar but the hole data is replaced and file become empty"
# a+ = " read and append the data get replaced "
# To find all the differences go! https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function
# Example 
# f=open("hello.txt","r")
# data=f.read()
# print(data)


# With 
# In with we assign the varaible at the end 
# Example
# with open("file name ","r") as f:
    # Statments
# Examples 
# with open("hello.txt","w") as f:
#     f.write("Hello World!")
# That varaible is called aliace and you do not have to close the file each time while using with as syntax it will do it automatically

# Module
# os    
# os is pre installed it is called operating system
# os.remove("file name")
# Example
# import os
# os.remove("hello.txt")

# Practice Question

# 1
# f=open("sample.txt","w")
# data=f.write("Hi everyone\nwe are learning file I/O \nusing java\nI like programing language")
# f.close()
# import os 
# os.remove("sample.txt")

# or 
# with open("sample.txt","w") as f:
#     data=f.write("Hi everyone\nwe are learning File I/O \nin java\nI like programing language")

# 2
# with open("sample.txt","r+") as f:
#     data=f.read()

# new_data=data.replace("java","python")
# print(new_data)

# with open("sample.txt","r+") as f:
#     f.write(new_data)

# 3
# with open("sample.txt","r") as f:
#     data=f.read()
# if(data.find("like")!=-1):
#     print("It exsists")
# else:
#     print("It does not exsists")

# 4
# with open("sample.txt","r") as f:
#     data=f.read()
# word=input("Enter the word you want to find ")
# print("Your data is available at :",data.find(word))
# if(data.find(word)==-1):
#     print("It does not exsists")

# 5
# def fnd_chr():
#     word="x"
#     data=True
#     line=1
#     with open("sample.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print("Data is at line ",line)
#                 return
#             line+=1
#     return -1 

# print(fnd_chr())

# import os
# os.remove("sample.txt")

# 6
# with open("num.txt","r") as f:
#     data=f.read()
#     num=""
#     for i in range(len(data)):
#         if(data[i]==","):     
#             num_data=int(num)
#             num=""
#             if(num_data%2==0):
#                 print("Number",num_data, "is Even")
#             else:
#                 print("Number",num_data, "is Odd")
#         else: 
#             num+=data[i]

# or
# with open("num.txt","r") as f:
#     data=f.read()
#     new_data=data.split(",")
#     print(len(new_data))

#     for i in range(len(new_data)):
#         num_data=int(new_data[i])
#         if(num_data%2==0):
#             print("Number is even",num_data)

