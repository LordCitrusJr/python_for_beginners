# Inheritance is creating a new class with information from another class, but then
# can define its own additional attributes and functions.
# The GameObject class in this example is considered the 'super class'
class GameObject:

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

# You can create functions in a class to give an object behaviors
    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

# In this example, the Enemy class is considered a subclass. Calling the GameObject in the parentheses inherits all
# of Game_objects attributes and functions.
# NOTE: The sub class has access to everything in the super class, but not vice versa.
class Enemy(GameObject):

    def __init__(self, name, x_pos, y_pos, health):
# Calling upon super here gives us access to everything in the GameObject super class
        super().__init__(name, x_pos, y_pos)
        self.health = health

    def take_damage(self, amount):
        self.health -= amount

game_object = GameObject("Game Object", 1, 2)
enemy = Enemy("Enemy", 5, 10, 100)

print(game_object.name)
print(enemy.name)
print(enemy.health)
enemy.take_damage(20)
print(enemy.health)
