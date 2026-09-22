""""
Task 4. Write a Python program to convert a given list of strings into list of lists using map 
function.
 """
 
def s_to_l(l):
    return list(l)

def string_to_list(l):
    
    result=map(s_to_l,l)
    return list(result)

sample = ['Red', 'Green', 'White', 'Black']

print(string_to_list(sample))