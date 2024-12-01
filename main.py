def longest_consecutive_ones(n):
  """
  Finds the length of the longest consecutive sequence of 1's in the binary representation of a number.

  Args:
    n: The number to convert to binary.

  Returns:
    The length of the longest consecutive sequence of 1's.
  """

  # Convert the number to binary
  binary_string = bin(n)[2:]

  # Initialize variables
  max_count = 0
  current_count = 0

  # Iterate through the binary string
  for bit in binary_string:
    if bit == '1':
      current_count += 1
      max_count = max(max_count, current_count)
    else:
      current_count = 0

  return max_count

# Get input from the user
number = int(input("Enter a number: "))

# Find the longest consecutive sequence of 1's
result = longest_consecutive_ones(number)

# Print the result
print("The length of the longest consecutive sequence of 1's is:", result)