"""
Task4
Create a program which will calculate the factorial

"""
# calculate factorial

def factorial():
    
    x = int(input("Insert the number u want to calculate its factorial: "))

    i =x
    result = 1

    while i >1:
        result *=i
        i-=1
    return "The factorial of {} is {}".format(x,result)  

print(factorial())
