# Objects are entities in code with related variables and functions.
# Classes act as blueprints for objects - defining the variables and functions. Classes use CamelCase
# an initializer function is a way to define the starting variables of a class
class GameObject:

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

# You can create functions in a class to give an object behaviors
    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

game_object = GameObject("Enemy", 1, 2)
print(game_object.name)
game_object.name = "Enemy 1"
print(game_object.name)

print(game_object.x_pos)
print(game_object.y_pos)

game_object.move(5, 10)

print(game_object.x_pos)
print(game_object.y_pos)

# We can create as many GameObjects as we want
other_game_object = GameObject("Player", 2, 0)
print(other_game_object.name)
print(other_game_object.x_pos)
print(other_game_object.y_pos)

# Objects we create are reference types. Other variables normally define (Int, Float, Boolean, "String")
# When we assign one equal to another, and change one of them, the other doesn't change
one_int = 5
another_int = one_int
print(one_int)
print(another_int)

another_int = 10
print(one_int)
print(another_int)

# Objects will refer to each other even if you change things around. aka creating references
other_game_object = game_object
print(other_game_object.name)

# A change in one will change in the other reference.
other_game_object.name = "new name"
print(other_game_object.name)
print(game_object.name)
