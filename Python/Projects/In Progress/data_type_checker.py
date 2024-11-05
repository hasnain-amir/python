def print_welcome_message():
    """Prints the welcome message for the user."""
    print("Welcome to the Data Type Checker and Formatter!")
    print("This tool will help you identify and format various data types in Python.\n")
    print("To get started, simply type in a value (like a number, string, or list) and hit Enter.")
    print("We'll tell you what type of data it is and give you options to format it if you'd like.")
    print("Let's dive in and explore your data together!")
    print("--------------------------------------------------")


def get_user_input(prompt="Please enter a value: "):
    """Prompts the user for input and returns it."""
    while True:
        user_input = input(prompt)
        if user_input.strip():  # Ensure input is not empty
            return user_input
        print("\033[38;5;214m" + "Input cannot be empty, please try again." + "\033[0m")  # Red text


def detect_data_type(value):
    """Detects and returns the data type of the given value along with a message."""
    # Check for Boolean
    if value.lower() in ['true', 'false']:
        return 'Boolean', "The data type is Boolean."

    # Check for specific data types
    if value.isdigit():  # Check for integer
        return 'Integer', "The data type is Integer."
    try:
        float(value)  # Check for float
        return 'Float', "The data type is Float."
    except ValueError:
        pass

    if value.startswith("[") and value.endswith("]"):  # Check for list
        return 'List', "The data type is List."
    elif value.startswith("{") and value.endswith("}"):  # Check for dictionary
        return 'Dictionary', "The data type is Dictionary."

    # If none of the above, it’s treated as a string
    return 'String', "The data type is String."


def format_string(value):
    """Formats a string by applying various transformations."""
    print("\nString Formatting Options:")
    print("1. Uppercase")
    print("2. Lowercase")
    print("3. Title Case")
    print("4. Strip Whitespace")
    print("5. Replace a Character")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        formatted = value.upper()
    elif choice == '2':
        formatted = value.lower()
    elif choice == '3':
        formatted = value.title()
    elif choice == '4':
        formatted = value.strip()
    elif choice == '5':
        old_char = input("Enter the character to replace: ")
        new_char = input("Enter the new character: ")
        formatted = value.replace(old_char, new_char)
    else:
        print("\033[38;5;214m" + "Invalid Choice." + "\033[0m")  # Red text
        return

    print(f"\033[38;5;214m" + f"Formatted String: {formatted}" + "\033[0m")  # Green text


def main():
    """Main program loop for the Data Type Checker and Formatter."""
    print_welcome_message()

    while True:
        print("\n\033[38;5;214m" + "Main Menu:" + "\033[0m")
        print("1. Check data type of a value")
        print("2. Format a string")
        print("3. Format a number (Unavailable for now)")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            user_input = get_user_input()
            detected_type, message = detect_data_type(user_input)
            print(f"\033[38;5;214m" + message + "\033[0m")  # Yellow text
        elif choice == '2':
            string_input = get_user_input()
            format_string(string_input)
        elif choice == '3':
            print("\033[38;5;214m" + "This is unavailable right now. Please try another option." + "\033[0m")  # Magenta text
        elif choice == '4':
            print("\033[38;5;214m" + "Thank you for using the Data Type Checker and Formatter. Goodbye!" + "\033[0m")  # Green text
            break
        else:
            print("\033[38;5;214m" + "Invalid choice. Please try again." + "\033[0m")  # Red text


# Run the main program loop
if __name__ == "__main__":
    main()


# Functions to Format Numbers
