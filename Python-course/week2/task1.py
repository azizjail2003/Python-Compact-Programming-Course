"""""
Task 1. Write a Python program  to get a list, sorted in increasing order by the last element in 
each tuple from a given list of non-empty tuples.  
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""
sample = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)] 

for i in range(len(sample)):
    for j in range(i+1,len(sample)):
        if sample[i][1]> sample[j][1]:
            sample[i],sample[j] = sample[j],sample[i]
    print(sample)           
            
print(sample)