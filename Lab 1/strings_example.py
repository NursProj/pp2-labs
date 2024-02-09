#1
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#2
a = "Hello, World!"
print(a[1])

#3
for x in "banana":
    print(x)

#4
a = "Hello, World!"
print(len(a))

#5
txt = "The best things in life are free!"
print("free" in txt)

#6
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#7
b = "Hello, World!"
print(b[2:5])

#8
a = "Hello, World!"
print(a.upper())

#9
a = "Hello, World!"
print(a.lower())

#10
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#11
a = "Hello, World!"
print(a.replace("H", "J"))

#12
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#13
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#14
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#15
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#16
