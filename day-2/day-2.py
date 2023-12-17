print("------Part 1------")

input = open ('day-2/input', 'r').read()

# input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

games = input.split("\n")
id_list = list()

for game in games:
    game_number, hands = game.split(":")
    hands = hands.split(";")
    valid = True
    for hand in hands:
        cubes = hand.split(",")
        for cube in cubes: 
            num, color = cube.split()
            if int(num) > 12 and color == "red":
                valid = False
            if int(num) > 13 and color == "green":
                valid = False
            if int(num) > 14 and color == "blue":
                valid = False
  
    if valid is True:
        name, id = game_number.split()
        id_list.append(int(id))

sum_id = sum(id_list)
print(sum_id)

print("-----Part 2-----") 

highest_num = list()
totals = list()

for game in games:
    game_number, hands = game.split(":")
    hands = hands.split(";")
    red_cubes = list()
    green_cubes = list()
    blue_cubes = list()
    for hand in hands:
        cubes = hand.split(",")
        for cube in cubes:
            num, color = cube.split()
            if color == "red":
                red_cubes.append(int(num))
            if color == "green":
                green_cubes.append(int(num))
            if color == "blue":
                blue_cubes.append(int(num))
    power_red = max(red_cubes)
    power_green = max(green_cubes)
    power_blue = max(blue_cubes)
    power = power_red * power_green * power_blue
    totals.append(power)
total = sum(totals)
print(total)
