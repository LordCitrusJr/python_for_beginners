# Control flow is checking a condition and executing a code if a condition is true while implementing logic into our code

# If statements are a basic form of control flow and are used to execute code if a condition is true
# Indentation is very important. The executable code must be below the If statement in order to run
key = "x"

if key == "r":
    print("move right")

# Else If is a combo of Else and If (elif). Keeps the If Statement going to check for
# additional conditions
elif key == "l":
    print("move left")

# Else statements will execute code if the If statement is false
else:
    print("invalid key")

print("done")

# Additional notes on If statements:
# * Can be nested in each other
if key == "r":
    print("move right")
    if key == "l":
        print("move left")
else:
    print("invalid key")

# * Can be used to check the condition of any type of variable
health = 1000
if health == 1000:
    print("max health")

# * Any operator can be used to check the condition (==, >, <, !=, >=, <=)
health = 1100
if health > 1000:
    print("over healed")
