
# Loops
# Loops are used to repeat instruction

# while Loops
# Syntax
# while condition:
    #some work
# Example
# x=3    Iterators
# while x<=5:
#     print("hello")    Iteration    
#     x+=1
# print(x)
# 2
# i=5
# while i>1:
#     print(i)
#     i-=1
# Traverse is going to the index value of list and tuple using loops

# Practice Question
# 1
# x=1
# while x<=100:
#     print(x)
#     x+=1

# 2
# x=100
# while x>=1:
#     print(x)
#     x-=1

# 3
# x=int(input("Enter the Number to find the table:"))
# y=1
# while y<=10:
#     print(x,"*",y,"=",x*y)
#     y+=1

# 4
# list=[1,4,9,16,25,36,49,64,81,100]
# x=1
# y=0
# while x<=10:
#     list[y]=x
#     x+=1
#     y+=1
# print(list)

# or
# list=[1,4,9,16,25,36,49,64,81,100]
# x=1
# y=0
# while x<=10:
#     print(list[y])
#     x+=1
#     y+=1

# or
# list=[1,4,9,16,25,36,49,64,81,100]
# x=0
# while x<len(list):
#     print(list[x])
#     x+=1

# or
# Its Finding the Square of all the numbers
# list=[1,4,9,16,25,36,49,64,81,100]
# x=1
# y=0
# while x<=10:
#     list[y]=print(int(list[y]/x))
#     x+=1
#     y+=1

# 5 
# list=[1,4,9,16,25,36,49,64,81,100]
# FindNumInList=int(input("Enter the number you want to find : "))
# if FindNumInList in list:
#     print("your Number is in the list")
# else:
#     print("Your number is not in the list")

# or
# list=(1,4,9,16,25,36,49,64,81,100)
# FindNumInList=int(input("Enter the number you want to find : "))
# a=0
# while a<len(list):
#     print(a,":",list[a]==FindNumInList )
#     a+=1

# or
# list=(1,4,9,16,25,36,49,64,81,100)
# numInlist=int(input("Enter your Number:"))
# a=0
# while a<len(list):
#     if list[a]==numInlist:
#         print("Your Number is in the list at index value of :",a)
#     a+=1

# or
# list=(1,4,9,16,25,36,49,64,81,100)
# numInlist=int(input("Enter your Number:"))
# a=0
# if numInlist in list:
#     while a<len(list):
#         if list[a]==numInlist:
#             print("Your number is in the list at index of :",a)
#             break
#         a+=1    
# else:
#     print("your number is not in the list")

# Break and Countinue
# Break
# Break ise use to break the loop under the given condition or can be used directly in the loop
# Countinue is use to skip the all statments it skip the statments in the loop if this is passed mostly used in if statments
# Example of break statment
# x=1
# while x<=5:
#     if(x==3):
#         print(3)
#         break
#     x+=1
# Example of Countinue statment
# x=1
# while x<=100:
#     if(x%2 == 0):
#         x+=1
#         continue
#     print(x)
#     x+=1

# For loop
# Loops are used for sequential traversal.For traversing list,string,tuples etc.
# Example
# list=[1,4,9,16,25,36,49,64,81,100]
# for element in list:
#     print(element)
# 2 
# tup=( 1,2,3,4,5)
# for num in tup:
#     print(num)
# 3
# name="ahmedwasim"
# for chr in name:
#     print(chr)
# You can also use else its called optional else
# Example
# name="abcdefghijklmnopqrstuvwsyz"
# for chr in name:
#     print(chr)
# else:
#     print("You have your abc")
# else is useful when if the loop get completly executed and did not get stopped or breaked by break statment 


# Prcatice Question
# 1
# list=[1,4,9,16,25,36,49,64,81,100]
# for num in list:
#     print(num)

# 2
# list=[1,4,9,16,25,36,49,64,81,100]
# x=1
# for num in list: 
#     getnum=num/x
#     print(int(getnum))
#     x+=1

# 3
# list=(1,4,9,16,25,36,49,64,81,100)
# fndnum=int(input("Enter the number you want to find: "))
# idx=0
# for num in list:
#     if(num==fndnum):
#         print("Number is found! at index of :" ,idx)
#         break
#     idx+=1    
# else:
#     print(fndnum,"number is not found!" )
# This process is called linear search

# Range
# Range functions returns a sequence of numbers , starting from 0 by default , and increments by 1 ( by default),and stops before a specified number.
# Range is the index value for index
# Example
# print(range(5))
# or
# seq=range(5)
# x=1
# while x!=5:
#     print(seq[x])
#     x+=1
# or
# seq=range(5)
# for num in seq:
#     print(num)
# or
# for num in range(10):
#     print(num)
# There are 3 ways to write range function
# In range only one number means stoping number 
# Example range(10) range(stop)
# If there is two it means there is start and stop
# Example range(5,10)  range(start,stop)
# If there is three numbers in the loop it means there is start ,stop and step 
# Example range(5,10,5) range(start,stop,step)
# Example making a script to print odd numbers
# x=input("Enter Even/Odd?:")
# if(x=="odd"):
#     x=1
# elif(x=="even"):
#     x=2
# for chknum in range(x,100,2):
#     print(chknum)

# Practice Question
# 1
# for num in range(1,101):
#     print(num)

# 2
# for num in range(100,0,-1):
#     print(num)

# 3
# num=int(input("Enter the number :"))
# for x in range(1,11):
#     print(num,"*",x,"=",num*x)

# Pass Statment In Loops
# Pass statment is used for the loop you do not want to execute any thing you can use pass
# Example
# for i in range(5):
#     pass
# print("Hello!")

# Practice Question

# 1
# n=int(input("enter num="))
# sum=0
# for i in range(1,n):
#     sum+=i
# print(sum)

# or
# n=int(input("enter num="))
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)

# 2 
# n=int(input("Enter the number you want to find Factorail:"))
# sum=1
# for i in range(1,n):
#     sum*=i
# print(sum)

