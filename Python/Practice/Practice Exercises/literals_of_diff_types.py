# Basic integer literals
int1 = 10
int2 = -50
int3 = 0

# Arithmetic operations with integers
add_result = int1 + int2          # Result: -40
sub_result = int1 - int3          # Result: 10
multiply_result = int2 * 5        # Result: -250
int_div_result = int1 // 3        # Result: 3 (integer division)
mod_result = int1 % 3             # Result: 1 (remainder)

# Display results
print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", multiply_result)
print("Integer Division:", int_div_result)
print("Modulus (remainder):", mod_result)

# -------------------------------------------------------------------------
print ("-------------------------------------------------------------------------")

# Basic float literals
float1 = 3.14
float2 = -0.001
float3 = 1.23e5  # Scientific notation, equivalent to 123000.0

# Arithmetic operations with floats
add_float_result = float1 + float2   # Result: 3.139
sub_float_result = float1 - 1.14     # Result: 2.0
mul_float_result = float1 * 2        # Result: 6.28
div_float_result = float1 / 2        # Result: 1.57

# Display results
print("Float Addition:", add_float_result)
print("Float Subtraction:", sub_float_result)
print("Float Multiplication:", mul_float_result)
print("Float Division:", div_float_result)

# Edge case: Precision with large and small floats
large_float = 1e16
small_float = 1e-10
precision_result = large_float + small_float  # Result may just show 1e16 due to precision limits

print("Precision Test (Large + Small):", precision_result)

# -------------------------------------------------------------------------
print("-------------------------------------------------------------------------")

# Basic string literals
str1 = "Hello, World!"
str2 = 'Python is fun!'
str3 = "He said, \"Welcome!\""
str4 = "First line\nSecond line"

# Print strings to see escape characters in action
print("Basic String:", str1)
print("With Escape Character:", str3)
print("Multi-line with \\n:\n", str4)

# String concatenation and repetition
concat_result = str1 + " " + str2  # Concatenate strings
repeat_result = str1 * 3           # Repeat string three times

print("Concatenated String:", concat_result)
print("Repeated String:", repeat_result)

# String indexing and slicing
first_char = str1[0]             # Access first character
substring = str1[7:12]           # Slice "World" from "Hello, World!"

print("First Character of str1:", first_char)
print("Substring of str1:", substring)

# Edge case: Accessing beyond string length (uncomment to test)
# invalid_index = str1[50]  # Raises IndexError
