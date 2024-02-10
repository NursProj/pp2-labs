#Boolean values
#1
print(10 > 9)
print(10 == 9)
print(10 < 9)

#2
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#3
print(bool("Hello"))
print(bool(15))

#4
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#5
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#6
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#7
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#8
def myFunction() :
  return True

print(myFunction())

#9
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#10
x = 200
print(isinstance(x, int))

#Operators
#1 - Multiply 10 with 5, and print the result.
print(10*5)
# 50

#2 - Divide 10 by 2, and print the result.
print(10/2)

#3 - Use the correct membership operator to check if "apple" is present in the fruits object.

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#4 - Use the correct comparison operator to check if 5 is not equal to 10.
if 5 != 10:
  print("5 and 10 is not equal")

#5 Use the correct logical operator to check if at least one of two statements is True.
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")

#Lists
#1 - Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
"""[apple]"""

#2 - Change the value from "apple" to "kiwi", in the fruits list
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
print(fruits)
"""['kiwi', 'banana', 'cherry']"""

#3 - Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)
"""['apple', 'banana', 'cherry', 'orange']"""

#4 - Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)
"""['apple', 'lemon', 'banana', 'cherry']"""

#5 - Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
"""banana"""

#6 - Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
"""cherry"""

#7 - Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
"""['cherry', 'orange', 'kiwi']"""

#8 - Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
"""3"""




