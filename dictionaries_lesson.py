# Dictionaries are more complex than lists and tuples. In lists and tuples,
# all of the elements have one value and are stored at specific indexes.
# In dictionaries, values are stored at keys. Meaning, for each element, we’ll have two values;
# the actual value and its key. Dictionaries use curly braces, not parentheses or brackets.
# dict = {key:value, key:value}
# Keys and Values can have any combination of variable type, i.e boolean:string, strings:integers,etc
actions = {"u": 1, "d": -1}
print(actions)

# We can modify the entire dictionary like a tuple.
actions = {"r": 1, "l": -1}
print(actions)

# We access elements based on their key. The syntax is similar to lists and tuple, but instead
# of their location, we use their key.

print(actions["r"])
print(actions["l"])

# the .get function searches the dictionary for a key. You'll receive an error if you try
# to access a key not in the dictionary.
print(actions.get("g"))

# On the other hand, if you try to modify a key that does not exist in the dictionary, it will not give
# an error, it will actually add the key and value to it. This negates the need for .append/.insert
actions["r"] = 2
actions["u"] = 1
print(actions)

# It is possible to print out the entire dictionary, just the keys, and or just the values.
# This is handy to check what values and keys exist.

# .keys: This function returns the keys in a dictionary
print(actions.keys())

# .values: This function returns the values in a dictionary
print(actions.values())

# .items: This function returns the entire dictionary
print(actions.items())

# There are two ways to remove items from dictionaries
# The del command  and .pop function will remove an item at a specific key
del (actions["u"])
print(actions)

actions.pop("r")
print(actions)

# The 'in' operator will check to see if an item is in a dictionary and return True or False
print("l" in actions)
