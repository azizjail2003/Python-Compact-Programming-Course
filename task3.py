
"""
Task3
Create a program that converts different data types and outputs the results.
1. Convert an integer to a floating-point number.
2. Convert a floating-point number to an integer.
3. Convert an integer to a string.
4. Convert a string containing a number to an integer.
5. Convert an integer to a Boolean
"""
def int_to_float():
    int_value= int(input("insert the integer value u want to convert to float: "))
    return print ("The type of {} is {}".format(float(int_value),type(float(int_value))))

def float_to_int():
    float_value = float(input("insert the float value u want to convert to int:" ))
    return print ("The type of {} is {}".format(int(float_value),type(int(float_value))))
def int_to_string():
    int_value = int(input("insert the int value u want to convert to string: " ))
    return print ("The type of {} is {}".format(str(int_value),type(str(int_value))))

def string_to_int():
    string_value = input("insert the string u want to convert to int: ")
    return print ("The type of {} is {}".format(int(string_value),type(int(string_value))))


def string_to_boolean():
    string_value = input("insert the string u want to convert to boolean: ")
    return print ("The type of {} is {}".format(bool(string_value),type(bool(string_value))))