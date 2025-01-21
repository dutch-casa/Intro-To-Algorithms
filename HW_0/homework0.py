'''
COMP 3270 Intro to Algorithms Homework 0: Introduction to Python
install python (google it) and make sure you have python version 3.6+ 
'''

# this is a single line comment just so you know

'''
This is a multi
line comment just fyi
'''

#Problem 1: print the string hello world to standard out
# your code here
print("hello world")

'''
Problem 2: declare variables with the types int, float, boolean, Nonetype and print their values and types
then perform operations additions, subtraction, multiplication, division, and power on the float and integer division and modulo on the int
'''
#your code here
int1 : int = 1
float1 : float = 1.0
bool1 : bool = True
None1 : None = None
print(type(int1))
print(type(float1))
print(type(bool1))
print(type(None1))
print(int1 + float1)
print(int1 - float1)
print(int1 * float1)
print(int1 / float1)
print(int1 ** float1)
print(int1 // float1)
print(int1 % float1)

'''
Problem 3: declare two strings and concatenate them
then print out the 2nd character to the last character without knowing the length of the string. 
'''
# your code here
str1 : str = "hello"
str2 : str = "world"
str3 : str = str1 + str2
print(str3)
print(str3[1:])


#Problem 4: Write a function that takes in a string name and prints out Hello, <name>!
#your code here
def hello(name):
    print("Hello, " + name + "!")

hello('Dutch')


'''
Problem 5: Write a function that takes in a number x and you compute and print out x! 
'''
#your code here
def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    print(result)

factorial(7)

'''
Problem 6: Write if statements to check if a number is postive, negative, or 0 and print a statement to that effect
'''
#your code here
def getSign(x):
    if x > 0:
        print("x is positive")
    elif x < 0:
        print("x is negative")
    else:
        print("x is 0")

getSign(12)

'''
Problem 7: Write a function that takes in a number x and prints out x^2
'''
#your code here
def square(x):
    print(x**2)

square(2)  

'''
Problem 8: Make a list of the squares of the numbers 0 to 9
add 100 to the end of that list
create another list with the square of the values 11 to 15 and concatenate those lists (show me 2 ways to do this)
check if the number 25 is in that list and print if it is
do the same with a list-comprehension to generate the list
create a dictionary where the keys are the numbers 0 to 9 and the values are the square of those numbers
create a set of the unique characters in a string
'''
#your code here
squares1 = [x**2 for x in range(10)]

squares1.append(100)

squares2 = [x**2 for x in range(11, 16)]

smush1 = squares1 + squares2  # Method 1: Using + operator
smush2 = squares1.copy()  # Method 2: Using .extend()
smush2.extend(squares2)

if 25 in smush1:
    print("25 is in the list")

list_comp = [x**2 for x in list(range(10)) + list(range(11, 16))]

if 25 in list_comp:
    print("25 is in the list comprehension")

squares_dict = {x: x**2 for x in range(10)}

testString = "hello world"
unique_chars = set(testString)
print(unique_chars)


'''
Problem 9: FizzBuzz
Write a function that takes in a list of numbers, loops over it and prints out Fizz if the number is a multiple
of 3, Buzz if it is multiple of 5, and FizzBuzz if it is a multiple of 3 and 5, otherwise print out the number
'''
#your code here
def fizzbuzz(numList):
    for num in numList:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


'''
Problem 10: Make a class called Person with attributes age and name
Make a method for that class called introduce which prints out an introduction with its name and age
Make an instance of that class and call its introduce method
'''
#your code here
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"How's it going? I'm {self.name} and I just turned {self.age}")

person1 = Person("Tacitus Kilgore", 30)
person1.introduce()



'''
Problem 11: install numpy, import it here and get the mean of a list of numbers and print it out
'''
import numpy as np
numbers = [1, 2, 3, 4, 5]

print(np.mean(numbers))