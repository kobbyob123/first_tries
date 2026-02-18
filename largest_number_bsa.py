# largest_number_bsa.py
# This is an implementation of the Bubble Sort Algortihm for small-sized lists

def largest(*numbers):
    """Returns the largest number in the list."""
    
    numbers_list = []
    
    # Storing the numbers in a list
    for number in numbers:
        numbers_list.append(number)
    
    # Get the length of this list
    n = len(numbers_list)
    
    # How to rearrange the numbers in the list without the sort() function
    for x in range(0, n):
        for y in range(0, n):
            if numbers_list[x] < numbers_list[y]:
                '''less than arranges it in ascending order,
                   greater than for descending order'''
                numbers_list[x], numbers_list[y] = numbers_list[y], numbers_list[x]
    
    # numbers_list.sort()
    
    # returns the largest number in the list
    return numbers_list[-1]

# Using function
from random import randint as rdint
nls = [rdint(0, 100) for x in range(10)]
bigOne = largest(nls)

print(str(nls) + " --> " + str(bigOne))
