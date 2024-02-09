#example
#1
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#2
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
#<class 'int'>

#3
x = 1    # int
y = 2.8  # float
z = 1j   # complex
#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#4
import random
print(random.randrange(1, 10))

#Exercise
#1
x = 5
x = float(x)

#2
x = 5.5
x = int (x)

#3
x = 5
x = complex(x)