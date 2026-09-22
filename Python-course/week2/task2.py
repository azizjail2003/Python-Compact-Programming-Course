"""""
Task 2. Given a string s1, write a program to return the sum and average of the digits that 
appear in the string, ignoring all other characters. 
 """


s1 = "AH13HXA-13SDAH238ADH1S"

def avg(s1):
    n=0
    sum=0
    for i in list(s1):
        if i.isdigit():
            sum = sum+int(i)
            n= n+1
    return sum,sum/n

print(avg(s1))