# Function to subtract two numbers
def subtract_numbers(a, b):
    return a - b

# Function to divide two numbers
def divide_numbers(a, b):
    return a / b

# Function to format a full name from first and last names
def format_full_name(first_name, last_name):
    return first_name + " " + last_name

# Test the subtraction function
result_subtract = subtract_numbers(10, 4)
print("Subtraction Result:", result_subtract)  # Expected output

# Test the division function
result_divide = divide_numbers(8, 2)
print("Division Result:", result_divide)  # Expected output

# Test the full name function
full_name = format_full_name("Hasnain", "Amir")
print("Full Name:", full_name)  # Expected output


# -------------------------

def add_numbers(item_price, tax_amount):
    return item_price + tax_amount

def calculate_tax(item_price, tax_rate):
    return item_price * tax_rate

def calculate_total_cost(item_price, tax_rate):
    tax_amount = calculate_tax(item_price, tax_rate)
    total_cost = add_numbers(item_price, tax_amount)
    return total_cost

item_price = 100
tax_rate = 0.2
total_cost = calculate_total_cost(item_price, tax_rate)
print ("The Total Cost: ", total_cost)