# Allow us to create blocks of reusable code. Use “def” to create a function.
# This allows us to choose exactly when and where to execute some code.
# It also allows us to input values as parameters and receive an output as a result.
position = 0

# Variables created inside a function can only be accessed inside the function, however,
# the global command allows a function to access variables defined outside of it.
def move_player():
    global position
    position += 1
    print(position)

# Remember to always define the function before you call it,
# otherwise you’ll receive an error as the function doesn’t exist
move_player()

# Parameters and Return Statements
position = 0

# We can create temporary values as Inputs through parameters, they help by fine-tuning functions.
# There can be many parameters # (separated by a comma) or you can give a function zero parameters
# by leaving the parentheses empty. Parameters can take on any variable type.
# The return keyword will end the function and return a value. This allows us to break out of a function,
# similar to break in loops.
def move_player(position, by_amount):
    position += by_amount
    return position

# Since we used a parameter when we created a function, it will be expecting us we call upon it inside the parentheses
position = move_player(position, 5)
print(position)
