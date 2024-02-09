#Example
#1
"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
#2
x = 5
print(type(x))

#3
"""
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType	
"""

#Exercise
#1
x = 5
print(type(x))
#<class 'int'>

#2
x = "Hello World"
print(type(x))
#<class 'str'>

#3
x = 20.5
print(type(x))
#<class 'float'>

#4
x = ["apple", "banana", "cherry"]
print(type(x))
#<class 'list'>


#5
x = ("apple", "banana", "cherry")
print(type(x))
#<class 'tuple'>

#6
x = {"name" : "John", "age" : 36}
print(type(x))
#<class 'dict'>

#7
x = True
print(type(x))
#<class 'bool'>


