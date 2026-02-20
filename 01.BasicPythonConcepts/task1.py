"""
Problem Statement: Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.

"""

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

add = first_number + second_number
sub = first_number - second_number
mul = first_number * second_number
div = first_number / second_number

print("Addition:", add )
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
