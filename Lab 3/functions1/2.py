#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature. The following formula is used for the conversion: C = (5 / 9) * (F – 32)
F = int(input("Fahrenheit = "))
def calculate(F):
    return ((5/9) * (F - 32))
print(calculate(F))