# Simple Quiz Application
# This program conducts a quiz with multiple-choice questions and tracks the user's score.

def welcome_message():
    """Prints the welcome message for the user."""
    print("\033[38;5;214m" + "Welcome to the Python Quiz Application" + "\033[0m")
    print("Test your knowledge of Python concepts with this fun and interactive quiz.\n")
    print("You will be presented with multiple-choice questions.")
    print("Select the correct answer by entering the corresponding number.")
    print("Let's see how well you know Python!")
    print("\033[38;5;214m" + "Good Luck!" + "\033[0m")

welcome_message()

def display_question(question, options):
    """
    Display a question and its options to the user, and return the user's selected answer.

    Parameters:
    question (str): The question to be displayed.
    options (list): A list of answer options.

    Returns:
    str: The user's selected answer from the options list.
    """
    print(question)  # Display the question

    # Display options with numbers
    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    while True:
        try:
            # Get user's answer
            answer = input("Please select an option (number): ")
            answer_index = int(answer) - 1  # Convert input to index

            # Validate the index
            if 0 <= answer_index < len(options):
                return options[answer_index]  # Return the selected option
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(options)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# List of questions, options, and correct answers
quiz_data = [
    {
        "question": "What is the output of the following code?\n\nx = 5\ny = 2.0\nprint(type(x + y))",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'list'>"],
        "correct_answer": "<class 'float'>"
    },
    {
        "question": "What will be printed by the following code?\n\ndef greet(name):\n    return f\"Hello, {name}!\"\n\nprint(greet(\"Alice\"))",
        "options": ["Hello!", "Hello, Alice!", "greet(Alice)", "None"],
        "correct_answer": "Hello, Alice!"
    },
    {
        "question": "What is the value of the following expression?\n\nresult = 10 % 3 + 2 * 5",
        "options": ["5", "6", "8", "7"],
        "correct_answer": "7"
    },
    {
        "question": "Which of the following statements is true about the variable a defined as a = [1, 2, 3]?",
        "options": ["a is a string.", "a is a tuple.", "a is a list.", "a is a dictionary."],
        "correct_answer": "a is a list."
    },
    {
        "question": "What will the following code output?\n\nnum = \"123\"\nconverted_num = int(num) + 5\nprint(converted_num)",
        "options": ["\"1235\"", "128", "1235", "TypeError"],
        "correct_answer": "128"
    },
    {
        "question": "What will be the value of z after the following code executes?\n\nx = 10\ny = 5\nz = x * y + y - x",
        "options": ["55", "45", "25", "0"],
        "correct_answer": "45"
    },
    {
        "question": "What does the following function return when called as add(3, 4)?\n\ndef add(a, b):\n    return a + b",
        "options": ["12", "7", "34", "None"],
        "correct_answer": "7"
    },
    {
        "question": "What will the following code output if num is set to 10?\n\nnum = 10\nif num > 5:\n    print(\"Greater than 5\")\nelif num < 5:\n    print(\"Less than 5\")\nelse:\n    print(\"Equal to 5\")",
        "options": ["Less than 5", "Equal to 5", "Greater than 5", "No output"],
        "correct_answer": "Greater than 5"
    }
]


# Initialise the score variable to track the user's score.

# Loop through each question in the quiz

# Display the final score to the user after all questions have been answered.