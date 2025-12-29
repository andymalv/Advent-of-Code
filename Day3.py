f = open("Day3.txt")
input = f.read()
f.close()

# %%
y = 0
x = 0
current_coordinates = [x, y]
visited_houses = [current_coordinates]
for i in range(len(input)):
    match input[i]:
        case "^":
            y += 1
        case "v":
            y -= 1
        case ">":
            x += 1
        case "<":
            x -= 1

    current_coordinates = [x, y]
    visited_houses.append(current_coordinates)

new_house = []
for house in visited_houses:
    if house not in new_house:
        new_house.append(house)

print(f"Unique houses visted: {len(new_house)}")

# %%
santa_y = 0
santa_x = 0
robo_y = 0
robo_x = 0
visited_houses = [[0, 0]]
for i in range(len(input)):
    if i % 2 == 0:
        match input[i]:
            case "^":
                santa_y += 1
            case "v":
                santa_y -= 1
            case ">":
                santa_x += 1
            case "<":
                santa_x -= 1

        santa_current = [santa_y, santa_x]
        visited_houses.append(santa_current)

    else:
        match input[i]:
            case "^":
                robo_y += 1
            case "v":
                robo_y -= 1
            case ">":
                robo_x += 1
            case "<":
                robo_x -= 1

        robo_current = [robo_y, robo_x]
        visited_houses.append(robo_current)

new_house = []
for house in visited_houses:
    if house not in new_house:
        new_house.append(house)

print(f"Unique houses visted: {len(new_house)}")
