# Simple Quiz Application
# This program conducts a quiz with multiple-choice questions and tracks the user's score.

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

# Initialise the score variable to track the user's score.

# Loop through each question in the quiz

# Display the final score to the user after all questions have been answered.