# Function to get squared values and separate them into odd and even lists
def get_squared_values(start, end):
    squared_values = [x**2 for x in range(start, end + 1)]
    odd_squares = [x for x in squared_values if x % 2 != 0]
    even_squares = [x for x in squared_values if x % 2 == 0]
    return odd_squares, even_squares

# Get user input for the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Get the squared values and separated lists
odd_squares, even_squares = get_squared_values(start, end)

# Output the results
print("Odd squares:", odd_squares)
print("Even squares:", even_squares)

