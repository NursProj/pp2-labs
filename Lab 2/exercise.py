#Boolean values
#1
print(10>9)
#true

#2
print(10==9)
#false

#3
print(10<9)
#false

#4
print(bool("abc"))
#true

#5
print(bool(0))
#false

#Operators
#1
print(10 + 5)
# "15"

#2
"""
Operator	Name	Example	
+	        Addition	x + y	
-	        Subtraction	x - y	
*	        Multiplication	x * y	
/	        Division	x / y	
%	        Modulus	x % y	
**	        Exponentiation	x ** y	
//	        Floor division	x // y
"""

#3
"""
Operator	Example	Same As	Try it
=	        x = 5	x = 5	
+=	        x += 3	x = x + 3	
-=	        x -= 3	x = x - 3	
*=	        x *= 3	x = x * 3	
/=	        x /= 3	x = x / 3	
%=	        x %= 3	x = x % 3	
//=	        x //= 3	x = x // 3	
**=	        x **= 3	x = x ** 3	
&=	        x &= 3	x = x & 3	
|=	        x |= 3	x = x | 3	
^=	        x ^= 3	x = x ^ 3	
>>=	        x >>= 3	x = x >> 3	
<<=	        x <<= 3	x = x << 3
"""

#4
print((6 + 3) - (6 + 3))
# 0

#5
print(100 + 5 * 3)
# 115

#6
print(5 + 4 - 7 + 3)
# 5


#Lists
#1
mylist = ["apple", "banana", "cherry"]

#2
thislist = ["apple", "banana", "cherry"]
print(thislist)
"""['apple', 'banana', 'cherry']"""

#3
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
"""['apple', 'banana', 'cherry', 'apple', 'cherry']"""

#4
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
"""3"""

#5
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
"""['apple', 'banana', 'cherry']"""
print(list2)
"""[1, 5, 7, 9, 3]"""
print(list3)
"""[True, False, False]"""

#6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
"""<class 'list'>"""

#7
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
"""['apple', 'banana', 'cherry']"""

#Tuples
#1 - Use the correct syntax to print the first item in the fruits tuple.
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
"""apple"""

#2 - Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))
"""3"""

#3 - Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
"""cherry"""

#4 - Use a range of indexes to print the third, fourth, and fifth item in the tuple.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Sets
#1 - Check if "apple" is present in the fruits set.
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#2 - Use the add method to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
"""{'cherry', 'banana', 'apple', 'orange'}"""

#3 - Use the correct method to add multiple items (more_fruits) to the fruits set.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)
"""{'cherry', 'mango', 'banana', 'apple', 'grapes', 'orange'}"""

#4 - Use the remove method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
"""{'apple', 'cherry'}"""

#5 - Use the discard method to remove "banana" from the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)
"""{'cherry', 'apple'}"""


#Distionaries
#1 - Use the get method to print the value of the "model" key of the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
"""Mustang"""
#2 - Change the "year" value from 1964 to 2020.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print(car.get("year"))
"""2020""" 

#3 - Add the key/value pair "color" : "red" to the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car["color"] = "red"
"""red"""

#4 - Use the pop method to remove "model" from the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)
"""{'brand': 'Ford', 'year': 1964}"""

#5 - Use the clear method to empty the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)
"""{}"""

#if...else
#1 - Print "Hello World" if a is greater than b.
a = 50
b = 10
if a>b:
    print("Hello World")

#2 - Print "Hello World" if a is not equal to b.
a = 50
b = 10
if a != b:
    print("Hello World")

#3 - Print "Yes" if a is equal to b, otherwise print "No".
a = 50
b = 10
if a == b:
    print("Yes")
else:
    print("No")

#4 - Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
a = 50
b = 10
if a==b:
    print("1")
elif a>b:
    print("2")
else:
    print("3")

#5 - Print "Hello" if a is equal to b, and c is equal to d.
a = 50
b = 45
c = 50
if a == b and c == b:
  print("Hello")

#6 - Print "Hello" if a is equal to b, or if c is equal to d.
if a == b or c == b:
  print("Hello")


#7 - Complete the code block, print "YES" if 5 is larger than 2.
#    Hint: remember the indentation.
if 5 > 2:
    print("YES")

#8 -  Use the correct one line short hand syntax to print "YES" if a is equal to b, otherwise print("NO").
a = 2
b = 5
print("YES") if a == b else print("NO")

#9 - Use an if statement to print "YES" if either a or b is equal to c.
a = 2
b = 50
c = 2
if a == c or b == c:
   print("YES")

#While loops
#1 - Print i as long as i is less than 6.
i = 1
while i < 6:
    print(i)
    i += 1

#2 - Stop the loop if i is 3.
i = 1
while i < 6:
    if i == 3:
        break
    i += 1

#3 - In the loop, when i is 3, jump directly to the next iteration.
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#4 - Print a message once the condition is false.
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#For loops
#1 - Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
"""
apple
banana
cherry
"""

#2 - In the loop, when the item value is "banana", jump directly to the next item.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

#3 - Use the range function to loop through a code set 6 times.
for x in range(6):
  print(x)

#4 - Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)