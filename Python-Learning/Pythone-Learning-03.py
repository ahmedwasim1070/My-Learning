# Dictionary and Sets

# Dictionary
# Dictionaries are uesd to store data values in key:value paris
# They are unordered,mutable (changeable)& don't allow duplicate keys
# Example
# dict={
#     "name": "ahmed",
#     "cgpa": 9.7,
#     "marks": [98,96,96],
#     "is-adult": True,
#     "age": 19,
#     "subjects": ("english","science","physice"),
# }
# You cannot repeat the key in dictionary
# print(dict["age"])
# print(dict["subjects"])
# dict["name"]="ali"
# print(dict["name"])
# dict["surname"]="Ahmed"
# print(dict)
# You can add all kind of data types in dictionary
# Nested Dictionary 
# There are also Nested Dictionary
# Which Means Dictionary in Disctionary
# info={
#     "name": "Muhammad Ahmad",
#     "subjects" :{
#         "comp": 59,
#         "phy" : 12,
#         "maths": 21,
#     },
#     "age": 19,
#     "CGPA": 3.5,
# }
# print(info["subjects"])

# Dictionary Method
# info={
#     "name": "Muhammad Ahmad",
#     "subjects" :{
#         "comp": 59,
#         "phy" : 12,
#         "maths": 21,
#     },
#     "age": 19,
#     "CGPA": 3.5,
# }
# Return all keys
# Return the keys
# print(info.keys())
# Type Casting
# In type casting it will remain dictionary but it will view as list
# print(list(info))
# print(type(info))
# Length of 
# print(len(info))
# or
# print(len(list(info.keys())))
# Values
# Return all values
# print(info.values())
# print(info["subjects"].values())
# Items
# Return all (key,val) pairs and tuples
# print(info.items())
# indexPrinting=list(info["subjects"].items())
# print(indexPrinting[1])
# print(indexPrinting[1][0])
# Get Method
# Returns the key according to value
# print(info.get("subjects"))
# print(info["subjects"])
# No difference but in case of misspelling .get method does not gives any error
# print(info.get("subject"))   Error
# print(info["subject"])    None
# The get method gives the None answer
# Update Method
# Insert the specified items to the dictionary
# info.update({"city" : "karachi"})
# print(info)

# Sets
# Sets is the collection of the unorderred items.
# Each element int the set must be unique & mutable.
# numbers={2,2,34.1,4,12,"ahmed"}
# print(numbers,type(numbers))
# If you add two same values it will not get duplicated
# You can add every data types except list and dictionary becaues they are mutable
# You cannot add empty set like dictionary one 
# To create empty set
# collection=set()
# Thats how you make empty set
# Sets Method
# Add method
# collection=set()
# collection.add(1)
# collection.add("ahmed")
# collection.add("wasim")
# print(collection)
# collection.add((1,2,"hello"))
# Remove method
# collection.remove("wasim")
# print(collection)
# Clear Method
# collection.clear()
# collecton clear will clear all the values from the set
# Pop Method
# Pop function randomly print the value
# print(collection.pop())
# Union Method 
# Union method works similar as Math union
# set={1,2,3,4}
# set2={2,3,4}
# print(set.union(set2))
# Intersection Method
# Intersecton also works similar as math intersection
# set={1,2,3,4}
# set2={3,5,6}
# print(set.intersection(set2))

# Practice Question

# 1
# meanings={
#     "table":("a piece of furniture","a piece of art"),
#     "cat ": "a small animal",
# }
# print(dictionary)

# 2
# set={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(set))

# 3
# marks={}
# marks.update({"comp": int(input("enter your comp number :"))})
# marks.update({"eng": int(input("enter your eng number :"))})
# marks.update({"phy": int(input("enter your phy number :"))})
# print(marks)    

#4
# num={9,"9.0"}


