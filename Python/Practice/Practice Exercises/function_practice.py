#Define basic functions with clear purposes (e.g. adding two numbers or printing a greeting)
   # - Call these functions with different arguments to see how they behave
#- Create functions that accept different types of inputs (int, string, lists etc).
   # - Experiment with calling these with various types of data to understand how they handle diff scenarios
#- Define functions that accept parameters and return values
   # - Test these functions by capturing their return values in variables and using those values in further calculations or function calls. 

# Simple Start
def add(a, b):
    return a + b
result = add(5, 6)
print(result)

# Varying input types
def check_data(data):
    if type(data) == int:       # If the input is a number
        return data + 10        # Add 10 to the number
    elif type(data) == str:     # If the input is a string
        return data.upper()     # Make the word uppercase
    elif type(data) == list:    # If the input is a list
        return data * 2         # Repeat the list twice
    else:
        return "Type not supported"    # If it's not a number, word or list
    
print(check_data(5))            # With a number: 5 + 10 = 15
print(check_data("Hello"))      # With a word: "hello" -> "HELLO"
print(check_data([1, 2, 3]))    # With a list: [1, 2, 3] repeated -> [1, 2, 3, 1, 2, 3]
print(check_data(3.14))         # Unsupported type -> "Type not supported"

# Accept parameters and return values
def calculate_area (length, width):
    area = length * width       # Calculate the area
    return area                 # Return the calculated area

area_of_rectangle = calculate_area(5, 3)    # length = 5, width = 3
print ("Area of rectangle: ", area_of_rectangle)   # Expected output: 15

cost_per_square_unit = 2
total_cost = area_of_rectangle * cost_per_square_unit    # Calculate the total cost

print("The total cost of flooring: ", total_cost)        # Expected output: 30

# Accepting parameters and return values with multiple functions

# Function to calculate the perimeter
def calculate_perimeter (length, width):
    return 2 * (length + width)

# Function to calculate both area and perimeter costs
def total_cost_of_fencing_and_flooring(area, perimeter, cost_per_square_unit, cost_per_unit_length):
    flooring_cost = area * cost_per_square_unit
    fencing_cost = perimeter * cost_per_unit_length
    return flooring_cost + fencing_cost

# Get area and perimeter
area = calculate_area(5, 3)
perimeter = calculate_perimeter(5, 3)

# Calculate the total cost
total_cost = total_cost_of_fencing_and_flooring(area, perimeter, 2, 5)
print("The total cost of flooring and fencing: ", total_cost)     # Expected output: 60