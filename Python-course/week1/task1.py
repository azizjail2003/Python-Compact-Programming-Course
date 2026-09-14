"""
Task1 
Create a program named `main.py`
Create a program which calculate the area of a circle

"""
from math import pi
def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    
    area = pi * (radius ** 2)
    return "The area of the circle with radius {:.2f} is {:.2f}".format(radius, area)

user_input = float(input("Enter the radius of the circle: "))

print(calculate_circle_area(user_input))