# Lists store values based on position (index). They start out like normal variables, but
# their data must be put into brackets, separated by a comma. Different variable types
# can be placed in the list
# example: name = [5, True, "string"]

enemy_positions = [5, 10, 15]
enemy_positions = [5, 10, 15, 20]
print(enemy_positions)

# When accessing one item in a list, it's zero-based meaning first item is at the zero position
print(enemy_positions[0])

# Trying to access a position that does not exist in the list, i.e. position 5 out of list size of 4,
# will return an 'index error' on the condole. To find out how many positions are in a given list,
# use the 'len' command

print(len(enemy_positions))

# Change a single value in a list by using brackets with the position between them.

enemy_positions[0] = 6
print(enemy_positions)

# Access a range of values in a list by using the brackets and positions separated by a colon. The upper
# bound is where it stops before, so to access the first two items in a list, use 0:2
print(enemy_positions[0:2])

# .append will add an item to the end of a list
enemy_positions.append(25)
print(enemy_positions)

# .insert will insert an item into a list at a specified position
enemy_positions.insert(1,9)
print(enemy_positions)

# .remove will remove a specific item in the list by its value
enemy_positions.remove(6)
print(enemy_positions)

# del will do the opposite of .insert and remove an item at a specified location
del enemy_positions[2]
print(enemy_positions)
