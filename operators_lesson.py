# Addition and Subtraction examples
x_position = 10
forward = x_position + 1
print(forward)
backward = x_position - 1
print(backward)

# Modulus example (returns the remainder of a division)
remainder = 5 % 2
print(remainder)

# Floor division example (discards the remainder of a division aka rounds down)
floor_division = 5 // 2
print(floor_division)

# Exponential example (raises a number to the power of another)
five_squared = 5 ** 2
print(five_squared)

# Shortcut to incrementally modify a variable (works with all arithmetic operators)
x_position += 1
print(x_position)

# Concantenation (appending strings) example
first_name = "Pepperoni "
last_name = "Pizza"
print(first_name + last_name)

# Conditional Operator Examples
x_position = 1
end_position = 10

# Equal to, greater or equal to
is_at_end = x_position == end_position
print(is_at_end)
is_at_halfway = x_position >= end_position / 2
print(is_at_halfway)

# Logical Operator Examples
# Not: The not operator negates a positive to a negative and vice versa.
not_is_at_end = not is_at_end
print(not_is_at_end)

# And: The 'and' operator checks if multiple things all the meet a condition
score = 10
is_game_over = score >= 10 and is_at_end
print(is_game_over)

# Or: The or operator checks if one, the other, or both items meets a condition
score = 10
is_game_over = score >= 10 or is_at_end
print(is_game_over)
