def split_bill(subtotal, num_friends):
    """
    Splits the bill among friends.
    
    Parameters:
    subtotal(float): The subtotal of the bill.
    num_friends (int): The number of friends to split the bill with.

    Returns:
    float: The amount each friend has to pay, rounded to two decimal places
    """
    # Calculate the total bill by adding 20% tax
    total_bill = subtotal * 1.20

    # Calculate the total bill per friend
    amount_per_friend = total_bill / num_friends

    # Return the amount rounded to two decimal places
    return round(amount_per_friend, 2)


# Example usage:
subtotal = 100.00
num_friends = 4
amount = split_bill(subtotal, num_friends)
print (f"Each friend has to pay: £{amount}")


    
