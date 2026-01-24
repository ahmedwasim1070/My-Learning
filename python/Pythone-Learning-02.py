

# Python Learning Lecture 02


# Strings
# String is a data type it stores a sequence of characters;
# You can create String by three ways 
# 1-In double quotes ""
# 2-In single quotes ''
# 3-In triple quotes """ """

# How to Give Next line in String in Pythone
# String1="This is a string \n This is the Next Line"
# print(String1);

# Concatenation
# Adding two Strings to one You can add the string by just using + plus sign
# a="Hello"
# b="Nigger"
# print(a+b);

# Finding Length of String
# len(str);   <--It is use to find the length of the string
# a="Ahmed";
# print(len(a));

# Indexing In String
# In pythone the first character index value will be zero 0 like js
# str="Ahmed wasim";
# print(str[5]);
# Space have also Indexing value unlike js

# Slicing
# Accessing part of the String
# Means breaking the string
# str="Ahmed Wasim"
# print(str[0:6])
# print(str[:6])
# print(str[6:len(str)])
# print(str[6:])
# In Pythone slicing there is also a negative Indexing 
# str="Mango";
# print(str[-3:-1]);
# print(str[-4:-2]);



# String Functions

# str="i am o studying python"
# print(str.endswith("python"));
# print(str.capitalize()); #In capitalize function it does not make the same string capital instead make a new one and capitallize the first letter to make the same string capitalize we can reasgin the same value in the same varaiable
# str=str.capitalize();
# print(str);
# print(str.replace("python","javascript"));
# print(str.find("a")) In case the letter does not exsit it will give the answer in the -1
# print(str.count("python"))


# Practice Question

# 1
# chkname=input("Your Name : ")
# print(len(chkname))

# 2
# var="Do you have $? I have 20$"
# chkvar=var.count("$")
# ckh=("false","true")[chkvar>=1]
# print(ckh)

# Nesting 
# A statment in a statment is called nesting

# Practice Question

# 1
# marks=float(input("Enter your makrs:"))
# if(marks<=100):
#     if(marks>=90):
#         print("Your Grade is A+")
#     elif(marks>=80):
#         print("Your Grade is A")
#     elif(marks>=70):
#         print("Your Grade is B")
#     elif(marks>=60):
#         print("Your marks is C")
#     elif(marks>=50):
#         print("Your marks is D")
#     else:
#         print("You are Eniligible ")
# else:
#     print("Enter Valid Marks")        

# 2
# chknumber=int(input("Chose a Number:"))
# if(chknumber%2==0):
#     print("Your number is even")
# else:
#     print("Your number is odd")

# 3
# a=int(input("Enter First Number : "))
# b=int(input("Enter your second number : "))
# c=int(input("Enter Third Number : "))
# if(a>b and a>c):
#     print("Your first is greater")
# elif(b>a and b>c):
#     print("Your second is gretaer")
# elif(c>a and c>b):
#     print("Your third is greater")
# else:
#     if(a==b==c):
#         print("All the number are the same")
#     elif(a==b):
#         print("your first and second are the same")
#     elif(a==c):
#         print("your first and third are the same")
#     elif(b==c):
#         print("Your Second and third are the same")

# 4
# a=int(input("Enter First Number : "))
# b=int(input("Enter your second number : "))
# c=int(input("Enter Third Number : "))
# d=int(input("Enter forth number:"))
# if(a>b and a>c and a>d):
#     print("Your first is greater")
# elif(b>a and b>c and b>d):
#     print("Your second is gretaer")
# elif(c>a and c>b and c>d):
#     print("Your third is greater")
# elif(d>a and d>b and d>c):
#     print("Your fourth is the largest")

# 5
# chknumber=int(input("Check the Number: "))
# if(chknumber%7==0):
#     print("Your number is a multiple of 7")
# else:
#     print("Your number is not a multiple of 7")

# List
# A built in data type that sotres set of values
# It can store elements of different type(integer,float ,string,etc.)
# Example
# marks=[12,34.52,60,89,"Fail"]
# print(type(marks))
# print(marks[4])
# print(len(marks))
# student=["ali",12,"5th class",89.9]
# print(student)
# Strings are Immutable means you can acess it but cannot change the value from the Indexing
# List are Mutable means you can acess and change the value by indexing

# Example
# student=["ali",12,"5th class",89.9]
# student[0]="hamza"
# print(student)

# List Slicing
# Slicing is also suppoted in list
# It is very similar with string slicing
# Example
# student=["ali",12,"5th class",89.9]
# print(student[1:3])
# print(student[:2])
# print(student[-3:-1])
# print(student[-3:])
# print(student[:-1])

# List Methods
# Append
# list=[1,2,3]
# list.append(4)
# print(list)
# Sorting
# list=[2,5,13,1]
# list.append(6)
# list.sort()
# print(list)
# list=[2,5,13,1]
# list.sort(reverse=True)
# print(list)
# list=["Apple","Mango","Bannana"]
# list.sort()
# list.sort(reverse=True)
# print(list)   Sorting is also applicable to string
# Reverse
# list=["a","b","c","d","e"]
# list.reverse()  Do not add the print with method it will return none
# print(list) It will reverse the order 
# Insert
# list=[2,5,13,1]
# list.insert(0,1)
# print(list)
# Remove
# list=[2,5,13,1]
# list.remove(5)
# print(list)
# Pop
# list=[2,5,13,1]
# list.pop(3)
# print(list)

# Tuples
# Tuples are immutable unlike List
# tup=(2,1,14,5)
# print(tup)
# print(tup[3])
# print(tup[2])
# tup[2]=2 This is wrong you cannot reasign it
# tup=("hello",2)
# print(tup)
# print(type(tup))
# Slicing in Tupple
# Slicing in tupple also possible and it works similarly
# Methods in Tupple
# Index
# Return the first occurance of the element
# tup=(1,235,545,235)
# print(tup.index(235))
# count
# Count the value how many time it occured
# tup=(1,235,545,235)
# print(tup.count(235))

# Practice Question

# 1
# a=input("Enter your first favourite movie:")
# b=input("Enter your second favourite movie:")
# c=input("Enter your Third Favourite Movie:")
# list=[]
# list.append(a)
# list.append(b)
# list.append(c)
# print(list)

# 2
# list=[1,"abc","abc",1]
# list2=list.copy()
# list2.reverse()
# if(list2==list):
#     print("palindrome")
# else:
#     print("non palindrome")

# list=[input("1:"),input("2:")]
# print(list)
# print(type(list))

# 3
# marksList=("A","B","A","F","D","A","C","A")
# print("The number of student with A grades are:" ,marksList.count("A"),type(marksList) )

# 4
# marksList=["A","B","A","F","D","A","C","A"]
# marksList.sort()
# print(marksList)
