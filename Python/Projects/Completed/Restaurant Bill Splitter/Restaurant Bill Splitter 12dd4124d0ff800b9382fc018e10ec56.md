# Restaurant Bill Splitter

<aside>
<img src="https://www.notion.so/icons/checklist_lightgray.svg" alt="https://www.notion.so/icons/checklist_lightgray.svg" width="40px" />

# Overview

This is my first project, it is basic. It adds the tax of the bill onto the subtotal, and then divides it between the number of friends. It then returns the total bill rounded to two decimal places.

# Key Features

- **Tax Calculation**: Automatically adds a 20% tax to the subtotal of the bill, providing an accurate total cost in the terminal output.
- **Terminal-Based Input**: Users can input the subtotal and the number of friends directly in the terminal, making it straightforward and accessible.
- **Even Split Calculation**: Divides the total bill evenly among the specified number of friends, simplifying the payment process without a graphical interface.
- **Rounded Results**: Displays the amount each friend needs to pay, rounded to two decimal places, ensuring clarity for financial transactions.
- **Simple Command-Line Interface**: Designed to be user-friendly within the terminal, allowing easy interaction without the need for advanced technical skills.
</aside>

#

# Tasks

[Tasks](Restaurant%20Bill%20Splitter%2012dd4124d0ff800b9382fc018e10ec56/Untitled%2012dd4124d0ff81bd85d9c148190a5051.csv)

<aside>
<img src="https://www.notion.so/icons/subtask_lightgray.svg" alt="https://www.notion.so/icons/subtask_lightgray.svg" width="40px" />

Code

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

</aside>

# Notes

[Untitled](Restaurant%20Bill%20Splitter%2012dd4124d0ff800b9382fc018e10ec56/Untitled%2012dd4124d0ff81268ab4d6a2577decc2.csv)

# Video

[https://youtu.be/4Y5dW85aTKc](https://youtu.be/4Y5dW85aTKc)
