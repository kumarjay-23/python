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
list1 = ["M","A","A","M"]
list = list1.reverse()
if(list == list1):
    print("palindrome")

    print("not palindrome")
#wap to count the number of students with the "A" grade in the following tuple 
#["C","D","A',"A","B","B","A"]

"""GRADE = ["C","D","A","A","B","B","A"]
print(GRADE.count("A"))"""

#store the above value in a list and sort them from "a" to "d"

"""GRADE = ["C","D","A","A","B","B","A"]
GRADE.sort()
print(GRADE)
"""
