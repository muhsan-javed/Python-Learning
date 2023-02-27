# import cv2
# import math

print(" Hello Programmer \n")
# print(5 + 8)
# print(math.gcd(3, 6))
# if(age<18){ // Not used this syntax java c c++ c# ...
# this is inside if
# }
# age = 18;
# if(age<23):
#     print("You age 18 yes")

# if age < 23:  # this new syntax
#     print("You age is greater than 18 you are allow")

a = 34
d = 6
b = "Muhsan"
c = 434.4213

# print(22.43+4321.23)
# print(a + d)
# print(a - d)
# print(a * d)
# print(a / d)

# Quiz: Try these operators:
# 1. ** Exponentiation operator
# 2. // Floor division operator
# 3. % Modulo operator

# Wrong syntax
# muhsan project =45
# Rules for creating variables
#  ---> 1: variable should start wioth a letter or an underscore
#  ---> 2: variable cannot start with a number
#  ---> 3: It can only contain alpha numeric characters
# ---> 4: variable names are case sensitive. Muhsan and Ali are two different variables

typeA = type(a)
typeB = type(b)
typeC = type(c)
typeD = type(d)
# print(typeA)
# print(typeB)
# print(typeC)
# print(typeD)
# print("\n\n\n\n")
e = 733
# print(e)

# names = '''Muhsan
# is a good boy
# Hello Programmer'''
# print(names+"\n\n\n")

# name = "Muhsan"
# print(age[2:6])
# print(age)
# print(age.strip())
# print(len(name))

# name = "Muhsan,Ali,tahmoor"
# var = name.lower()
# var = name.upper()
# var = name.replace(",","\n")
# print(var)
str = "This is a "
name = "Muhsan"
name1 = "Ali"  # E.g
str2 = "This is not a"
# print(str+name)
# temp = "This is a {0} and he is a good boy named {1}".format(name,name1) # Default value
temp = f"This is a {name} and he is a good boy named {name1}"
# print(temp)

'''
# Python Collections:
1. List
2. Tuple
3. Set
4. Dictionary

'''
# List
lst = [23, 435, 76, 98, 43, 325, 767, 868, 6]
# var = type(lst)
# lst[8] = 34
# var = lst[8]
# lst.append(100)
# lst.insert(1,100)
# lst.remove(868)
# lst.pop()
# del lst[2]
# lst.clear()
# var = lst
# var = len(lst)
# var = lst[1:8]
# print(var)

# Tuple
a = ["Muhsan", "Ali", "Hyder", "Uzair"]
# var = a
a = list(a)
var = type(a)

# Cannot do this
a[0] = "NEw"
# print(var)

# Set
s1 = {1, 23, 32, 4, 5, 5, 5, 5, 5, 5, 3}
# s1.add(444444)
# s1.update([12,23,54,56,34,24,24,12,65,56,23,12])
# print(len(s1))
# s1.remove(16666)
# Like list you can use : .pop, .clear ,.del, .intersection, union
# s1.discard(358345)
# print(s1)

# Dictionary

muhsanDict = {
    "Name": "Muhsan",
    "Class": "3th",
    "Marks": 43.56,
    "Hours in School": 4
}
# print(muhsanDict)
muhsanDict["Marks"] = 90
muhsanDict.pop("Marks")
# del, clear, pop , update,
# print(muhsanDict["Marks"])

# age = 54
# age = input("Enter your age\n")
# age = int(age)
# print(type(age))
# if(age>18):
#     print("Your can drive a car")
# elif(age == 18):
#     print("You are allow now")
# elif(age==15):
#     print("Sorry you are not allow")
# else:
#     print("You cannot drive")

# Loops:
# Scenario: you have to print numbers between 1 to 100
li = [23, 545, 65, 7, 57, "this"]
# for item in li:
#     print(item)


# for i in range(1,100):
#     print(i)
# Quiz: use for loop to iterate dictionary, set and tuples

# i = 0
# while(i<100):
#
#     if i == 90:
#         # break
#         continue
#     print(i + 1)
#     i = i + 1

# Functions:
# def greet():
#     print("Good morning sir")
# greet()
def sum(a, b):
    # print("Running sum")
    c = a + b
    return c


d = sum(43, 7)
# print(sum(34,6))
# print(d)

class Employee:
    def __init__(self, name, gsalary):
        self.name = name
        self.salary = gsalary

muhsan  = Employee("Muhsan",45)
print(muhsan.name)
print(muhsan.salary)
