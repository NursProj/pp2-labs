#Function
#1 - Create a function named my_function.
def my_function():
  print("Hello from a function")

#2 - Execute a function named my_function.
def my_function():
  print("Hello from a function")
# my_function()

#3 - Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
  print(fname)

#4 - Let the function return the x parameter + 5.
def my_function(x):
    return x+5

#5 - If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
# def my_function(*kids):
#   print("The youngest child is " + kids)

#6 - If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?
def my_function(**kid):
  print("His last name is " + kid["lname"])


#Lambda
#1 - Create a lambda function that takes one parameter (a) and returns it.
x = lambda a : a

#2 - Create an object of MyClass called p1:
class MyClass:
    x = 5
p1 = MyClass()

#3 - Use the p1 object to print the value of x:
class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

#4 - What is the correct syntax to assign a "init" function to a class?
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age