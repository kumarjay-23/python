#lecture: 1 , variable and data types
# write a program to input 2 number and print their sum
"""first = int(input("enter first : "))
second = int(input("enter second : "))
print ("sum = " , first + second)
"""
#WAP to input side of a square and prints its area

"""side =float(input("side : "))
area = print("area : " , side*side) 
"""
# WAP to iput 2 floating point numbers & print their average

"""a = float(input("a = "))
b = float(input (" b = "))
 
print("avg = " , (a+b)/2)
"""
#wap to input 2 int numbers a and b. print true if a is greater than or equal to b . if not print false

"""first = int(input("enter first : "))
second = int(input("enter second : "))
print(first>=second)"""


# lecture ; 2 , strings and conditional statements

# wap to check if a number entered by the user is odd or even.

"""num = int(input("num : "))
if(num % 2 == 0 ):
    print("even")
else:
    print(odd)"""

# wap to find the greatest of 3 number enterd by the user

"""first = int(input("enter first : "))
second = int(input("enter second : "))
third = int(input("third ; "))
if(first>second and first>third):
    print("first is greater",first)
elif (second>third):
        print("second is greater",second)
else:
        print("third is greater",third)
"""


# wap to check if a number is a multiple of 7 or not

"""num = int(input("num;"))
if (num % 7 == 0):
    print ("multiple of 7")
else:
    print ("not multiple of 7")
"""
    # wap to ask the user to enter names of their 3 favourite movies and store them in a list
"""a = input("movie 1: ")
b =input("movie 2: ")
c =input("movie 3: ")

list = [a,b,c]
print(list)"""

#wap to check if a list contains a palindrome of elements
"""list1 = ["M", "A", "A", "M"]
rev_list = list1.copy()   # Make a copy
rev_list.reverse()        # Reverse the copy
if list1 == rev_list:
    print("Palindrome")
else:
    print("Not a palindrome")"""
    
#wap to count the number of students with the "A" grade in the following tuple 
#["C","D","A',"A","B","B","A"]

"""GRADE = ["C","D","A","A","B","B","A"]
print(GRADE.count("A"))"""

#store the above value in a list and sort them from "a" to "d"

"""GRADE = ["C","D","A","A","B","B","A"]
GRADE.sort()
print(GRADE)
"""
# store the following word meanings in a python dictionary:
# table : " a piece of furniture","list of facts and figures"
# cat : "a small animal"

"""dictionary = {
    "cat": "a small animal",
    "table": [" a piece of furniture","list of facts and  figures "]
}

print(dictionary)"""

#you are given a list of subjects for students .assume one classroom is required for 1 subject.
#how many classrooms are needed by all students
#"#python","java","c++","python","javascript","java","python","java","c++","c"

"""subjects= {
    "python","java","c++","python","javascript","java","python","java","c++","c"
  }
print(len(subjects))"""

#wap to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary and
#  add one by one.use subject name as key and marks as value.
"""marks = {}
x = int(input("enter phy : "))
marks.update({"phy": x})
x = int(input("enter math : "))
marks.update({"math": x})
x = int(input("enter che : "))
marks.update({"che ":x})
print(marks)"""

#figure out a way to store 9 and 9.0 as seperate values in the set.

"""values = {
    ("float",9.0),
    ("int",9)
}
print(values)"""

#print number from 1 to 100

"""i=1
while i <= 100:
    print(i)
    i += 1"""

#print number from 100 to 1

"""i = 100
while i >= 1:
    print(i)
    i -= 1"""

#print the multiplication table of a number n 

"""n = int(input("enter number : "))
i = 1
while i <= 10:
    print(n*i)
    i += 1"""

#print the elements of the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]

"""nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

"""

#
