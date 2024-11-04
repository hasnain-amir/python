import json

def print_welcome_message():
    """Prints the welcome message for the user."""
    print("Welcome to the Data Type Checker and Formatter!")
    print("This tool will help you identify and format various data types in Python.\n")
    print("To get started, simply type in a value (like a number, string, or list) and hit Enter.")
    print("We'll tell you what type of data it is and give you options to format it if you'd like.")
    print("Let's dive in and explore your data together!")
    print("--------------------------------------------------")

def get_user_input():
    """Prompts the user for input and returns it."""
    while True:
        user_input = input("Please enter a value to check its data type: ")
        if user_input.strip():  # Ensure input is not empty
            return user_input
        print("Input cannot be empty, please try again.")

def detect_data_type(value):
    """Detects and prints the data type of the given value."""
    # Check for Boolean
    if value.lower() in ['true', 'false']:
        print("The data type is Boolean.")
        return 'Boolean'

    # Check for List or Dictionary using json.loads for better parsing
    try:
        parsed_value = json.loads(value)
        if isinstance(parsed_value, list):
            print("The data type is List.")
            return 'List'
        elif isinstance(parsed_value, dict):
            print("The data type is Dictionary.")
            return 'Dictionary'
    except json.JSONDecodeError:
        pass  # Not a valid list or dict format

    # Try to check for Integer or Float
    try:
        int_value = int(value)
        print("The data type is Integer.")
        return 'Integer'
    except ValueError:
        try:
            float_value = float(value)
            print("The data type is Float.")
            return 'Float'
        except ValueError:
            # If it passes all checks, it must be a String
            print("The data type is String.")
            return 'String'

# Main execution
if __name__ == "__main__":
    print_welcome_message()  # Print the welcome message
    user_input = get_user_input()  # Get user input once
    detect_data_type(user_input)    # Detect and print the data type

# Main program loop



# Functions to Format Strings



# Functions to Format Numbers




# Function for Menu Interface