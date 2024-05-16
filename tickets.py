def tickets(*tickets):
    """Returns the total amount to pay."""
    group = []
    fee = 1000
    total = 0
    
    # Adding the ages to a group
    for ticket in tickets:
        group.append(ticket)

    # Calculating the total amount to pay
    for age in group:
        if age < 3:
            continue
        else:
            total = total + fee
    return total
