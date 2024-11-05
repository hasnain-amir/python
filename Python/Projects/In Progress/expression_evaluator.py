def welcome_message():
    print("\033[38;5;214m" + "Welcome to the Expression Evaluator!" + "\033[0m")
    print("This command-line tool will help you evaluate mathematical expressions.")
    print("You can enter any expression, and the tool will parse and evaluate it for you.")
    print("This is a great way to practice writing expressions and understanding how Python evaluates them.")
    print("Type 'exit' to quit the program.")
    print("Let's get started!\n")

welcome_message()

# Input Functionality (Function to prompt for user input)
def get_user_input():
    while True:
        user_input = input("\033[38;5;214m" + "Enter a mathematical expression (or type 'exit' to quit): " + "\033[0m")
        if user_input.lower() == 'exit':  # Ensure case insensitivity
            print("\033[38;5;214m" + "Exiting the Expression Evaluator. Goodbye!" + "\033[0m")
            break
        else:
            # Placeholder for the expression evaluation function
            # evaluate_expression(user_input)
            print(f"You entered: {user_input}\n")  # Echo the input for now

# Call the input function to start prompting for input
get_user_input()

# Expression Evaluation (Function to evaluate expression)

# Error Handling (Function to handle evaluation errors)

# History Feature (Function to track previous evaluations)

# Looping until exit is already handled in get_user_input