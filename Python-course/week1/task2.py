"""
Task2
Create a program that stores an integer, a floating-point number, a string, and a boolean
variable, and then outputs them.

Declare and initialize an integer variable `zahl` with the value 10. Check the variable's type
afterward.

Declare and initialize a floating-point variable `kommazahl` with the value 10.5. Check the
variable's type afterward.

Declare and initialize a string variable `text` with the value "Hello, World!". Check the
variable's type afterward.

Declare and initialize a boolean variable `wahrheitswert` with the value True. Check the
variable's type afterward.
Output all variables
"""
# variable declarations and initializations
zahl = 10
kommarzahl = 10.5
text = "Hello, World!"
wahrheitswert = True
# print the variables and their types
print("Integer variable 'zahl' : {}, Type: {}".format(zahl, type(zahl)))
print("Floating-point variable 'kommarzahl': {}, Type: {}".format(kommarzahl, type(kommarzahl)))
print("String variable 'text': {}, Type: {}".format(text, type(text)))
print("Boolean variable 'wahrheitswert': {}, Type: {}".format(wahrheitswert, type(wahrheitswert)))