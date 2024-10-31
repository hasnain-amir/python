# Restaurant Bill Splitter

# Overview

This is my first project, it is basic. It adds the tax of the bill onto the subtotal, and then divides it between the number of friends. It then returns the total bill rounded to two decimal places.

# Key Features

- **Tax Calculation**: Automatically adds a 20% tax to the subtotal of the bill, providing an accurate total cost in the terminal output.
- **Terminal-Based Input**: Users can input the subtotal and the number of friends directly in the terminal, making it straightforward and accessible.
- **Even Split Calculation**: Divides the total bill evenly among the specified number of friends, simplifying the payment process without a graphical interface.
- **Rounded Results**: Displays the amount each friend needs to pay, rounded to two decimal places, ensuring clarity for financial transactions.
- **Simple Command-Line Interface**: Designed to be user-friendly within the terminal, allowing easy interaction without the need for advanced technical skills.
</aside>

# Code

```python
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
```

# Video

[See it in Action!](https://youtu.be/4Y5dW85aTKc)
