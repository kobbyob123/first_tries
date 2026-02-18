def calc_tickets(*ages):
    """
    Calculates the total amount to pay for a group of people based on their ages.

    Args:
        *ages: A variable number of age arguments.

    Returns:
        int: The total amount to pay.
    """
    fee = 10
    total = 0
    
    '''
    Adding the ages to a group
    for age in ages:
       group.append(age)

    Calculating the total amount to pay
    group = []
    for age in group:
        if age <= 3:
            continue
        else:
            total += fee
    '''
    
    total = sum(fee for age in ages if age > 3)
    return total

gp1 = calc_tickets(23, 45, 21, 2, 1, 3)

print("The group total is {}".format(gp1))
