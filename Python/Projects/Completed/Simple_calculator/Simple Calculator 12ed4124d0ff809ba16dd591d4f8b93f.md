# Simple Calculator

## Overview

This command-line calculator performs basic arithmetic operations, including addition, subtraction, multiplication, and division. It features a user-friendly interface that allows users to input two numbers and select an operation. Additionally, the calculator keeps a history of calculations and provides an option to clear the history. Designed for quick and efficient use in a terminal environment, this calculator is perfect for anyone needing fast calculations on the go.

</aside>

<aside>
<img src="https://www.notion.so/icons/subtask_lightgray.svg" alt="https://www.notion.so/icons/subtask_lightgray.svg" width="40px" />

## Key Features

- **Basic Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **User Input**: Prompts users for two numbers and the desired operation.
- **Calculation History**: Keeps a record of previous calculations for easy reference.
- **Clear History Option**: Allows users to reset the calculation history as needed.
- **Error Handling**: Handles invalid inputs and division by zero gracefully.
- **Interactive Interface**: Enables continuous calculations until the user decides to exit.
</aside>

## Code

```python
# History Feature
history = []  # At the top of your program

# Arithmetic Operations Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

# User Input Function
def get_user_input():
    while True:
        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))
            operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
            return first_number, second_number, operation
        except ValueError:
            print("Invalid input. Please enter numeric values for the numbers.")

# Function to Perform Calculations
def perform_calculation(first_number, second_number, operation):
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    function = operations.get(operation)
    if function:
        return function(first_number, second_number)
    else:
        return "Invalid operation!"

# Display Function
def display_result(result, operation, first_number, second_number):
    print(f"\nThe result of {operation} {first_number} and {second_number} is: {result}\n")
    print("History of calculations:")

    if history:  # Check if history is not empty
        print(f"{'No.':<5} {'Calculation':<30}")  # Header for history
        print("-" * 35)  # Separator line
        for index, entry in enumerate(history, start=1):  # Enumerate for numbering
            print(f"{index:<5} {entry:<30}")  # Format each entry
    else:
        print("No calculations have been made yet.")

# Clear History Function
def clear_history():
    history.clear()  # Clear the history list
    print("Calculation history has been cleared.")

# Main Program Loop
def main():
    while True:
        first_number, second_number, operation = get_user_input()
        result = perform_calculation(first_number, second_number, operation)

        if isinstance(result, (int, float)):
            history.append(f"{first_number} {operation} {second_number} = {result}")

        display_result(result, operation, first_number, second_number)

        # Option to clear history
        clear_option = input("Do you want to clear the history? (yes/no): ").strip().lower()
        if clear_option == "yes":
            clear_history()

        continue_calculating = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if continue_calculating != "yes":
            break

if __name__ == "__main__":
    main()
```

</aside>

## Video

[View it in Action!](https://youtu.be/IgCQlzV25b4)
