# While loops are the simplest form of loops. It will run a block of code until a condition is False
position = 0
end_position = 10
enemy_position = 5

while position < end_position:
    position += 1
    print(position)
# The way which we construct loops is dependent on what the end goal is. We can use two commands to additionally
# control when we exit or interject loop iterations; break and continue
# Break is used to break prematurely exit a loop
    if position == enemy_position:
        print("Game Over!")
        break

if position == end_position:
    print("You have reached the end.")

# Continue control example
position_two = 0
end_position_two = 10
enemy_position_two = 5

# Continue is used to interject into a loop on a condition
while position_two < end_position_two:
    position_two += 1
    print(position_two)
    if position_two == enemy_position_two:
        print("Enemy Encountered!")
        continue

if position_two == end_position_two:
    print("You have reached the end.")
