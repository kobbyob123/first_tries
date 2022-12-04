# This is a program to find the largest number in a list
# This involves the use of the bubble sort algorithm

def largest(*numbers):
    """Returns the largest number in the list."""
    group = []
    for number in numbers:
        group.append(number)
    n = len(group)
    # group.sort()
    # How to rearrange the numbers in the list without the sort() function
    for x in range(0, n):
        for y in range(0, n):
            if group[x] < group[y]:
                '''less than arranges it in ascending order,
                   greater than for descending order'''
                group[x], group[y] = group[y], group[x]
    return group[n-1]
