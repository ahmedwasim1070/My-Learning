

# Python Learning 

# Varaiable Declaration

# name = "ahmed";
# age=19;
# status="unemployed";
# print ("my name is :",name,"my age is :",age,status);

# Thats how you get the type of the variable
# print(type(age));    its type is integer

# Test Question

# print(123421421+12321321321);

# or

# a=123;
# b=321;
# sum=a+b;
# print(sum);

# or

# a=123;
# b=321
# print(a+b);

# Multiplying String with integers 
# But you cannot multiply integer with string
# You cannot add the string and integers but you can multiply them by multiplying it gives the following answer 

# a,b=12,5;
# c="@";
# print(a*c*b);
# It will always multiply the string to multiple 

# You can add two string tho like two integers and floats

# a,b="2",5;
# c="nigga";
# print((a+c)*b);

# There are two types of Divisions

# There is a simple division where you get the answer like simple division but point to be noted that you will always get the answer in float which is different from integers
# a,b=5,10;
# c=a/b;
# print(c)

# There is a Integer division which is work like javascript floor function which is use to round off the number but it always round off to lower number 
# a,b=1.5,3
# c=a//b; Float Function also know as
# print(c,a/b);


# Remainder Using Module % 

# If the denomenator of the divsion is negative the answer will be in negative while if the nomenator of the division is negative and denomenator is positive then the answer will always be in positive
# % <---This symbol is called module and used for extracting the remainder of the division with the a little different rule where the denomenator have more importance then nemenator in sign only.
# Example

# a,b=5,2;
# c=a%b;  The Sign of denomenator maters while neumenator does no matter
# print(c);

# a,b=5,-2;
# c=a%b;
# print(c);

# """a,b=-5,2;
# c=a%b;
# print(c);"""



# Types of Comment in Python
# first with hash and second with triple double quoted comas """

# Inputs In Python

# String Input 
# Input always take the value in sting so we have to convert it into integer or float or other you have to use type casting
# name=input("name : ")
# print(name);

# Int Input and Float Input
# To convert the string to integer it should be number tho so inorder to make it integer you need to add int before the input and similarly You have to insert float inorder to convert it into float
# age=int(input("age: "));
# age2=float(input("age: "));
# print(age,age2);

# Practice Question

# Input Question
# name=input("name: ");
# age=int(input("age : "));
# semester=float(input("class :"));
# print("My name is :",name,"My age is : ",age, "and i study in :",semester);
# print(type(name),type(age),type(semester));

# Python is an indentation
# Indentation refers to giving the spacing before starting the statment does matter in python unlike javascript it does not matter
  
# Conditional Statments 

# if-elif-else(syntax)

# if(condition):  we can also add multiple if 
    # Statment1
# elif(condition):  we can also add multiple elif
    # statment2
# else:
    # statmentN   we can only else only one time

# Practice Question for Conditional Statment

# light=input("light: ");
# if(light=="red"):
#     print("stop");
# elif(light=="yellow"):
#     print("start");
# elif(light=="green"):
#     print("go");
# else:
#     print("light is broken ");

# Quetion 2 

# marks=int(input("marks : "));
# if(marks>=90):
#     print("A+");
# elif(marks>=80 ):
#     print("A");
# elif(marks>=70):
#     print("B");
# elif(marks>=60):
#     print("C");
# elif(marks>=50):
#     print("D");
# else:
#     print("you are a failure you can never make it ");

# Writing Conditional Statment in Short form

# First way of writing
# The Synta of Writing
# You can store the whole conditional statment in the variable the the statment then the condition you can also add operotrs to act it as the condition and in the end you can also add the else 
# number= int(input("number : "));
# var = "Number is in tens" if number>=10 else "Number is not in tens"
# print(var)

# Second way of writing
# The Syntax is that 
# First the statment then the condition you can add or and or not or other operators in it to make it work like elif 
# number=int(input("number : "));
# print("Number is greater or smaller so it can not be displayed") if number>=10 or number==0 else print(number);

# Another type of Conditonal statment 
# Clever if is an ternary operator
# Syntax
# variable=(false statment,true statment)[condition]

# Example
# age=int(input("age: "));
# var=("You are Under age","You are above 18 Enjoy!")[age>=18]
# print(var);

# Example
# sal=float(input("salary:"));
# tax=sal*(0.1,0.2)[sal<=50000]
# print(tax);

# Types of Operators 

# Arithmetic Operators
# (+,-,*,/,%,**)

# Relational Operator
# Relational operator gives the value in bolean true or false
# (==,!=,>,<,>=,<=)

# Assigment Operator
# (=,+=,-=,*=,/=,%=,**=)

# Logical Operators 
# Logical Operators works on Bolean value 
# (not,or,and)



# Type Conversion

# Conversin
# float>>integer
# a=12;
# b=10.5
# sum=a+b;
# print(sum);

# Casting
# a=float("1");
# b=3.12
# sum=a+b;
# print(sum);
# print(type(a));

# Practice Question
# a=int(input("Enter Your first Number:"));
# b=int(input("Enter Your Second Number:"));
# print(a+b);

# Question-2
# height=int(input("Enter the height of square:"))
# base=int(input("Enter the base of the square:"))
# area=height*base;
# print(area,"cm");

# Question-3
# a=float(input("enter the first number:"))
# b=float(input("enter the second number:"))
# average=(a+b)/2;
# print(average);

# Question-4
# a=int(input("Enter your Number :"))
# b=int(input("Enter your 2nd Number :"))
# print(a>=b);

