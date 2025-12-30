import numpy as np

f = open("Day6.txt")
input = f.read().splitlines()
f.close()

# %%
grid = np.zeros([1000, 1000])
for index, instruction in enumerate(input):
    for k, c in enumerate(instruction):
        if c.isdigit():
            first_num = k
            break

    coords = instruction[first_num:].split(" through ")
    start_x = int(coords[0].split(",")[0])
    start_y = int(coords[0].split(",")[1])
    start = [start_x, start_y]
    end_x = int(coords[1].split(",")[0])
    end_y = int(coords[1].split(",")[1])
    end = [end_x, end_y]

    if instruction.find("turn on") != -1:
        for row in range(start[0], end[0] + 1):
            for col in range(start[1], end[1] + 1):
                if grid[row, col] == 0:
                    grid[row, col] = 1
    elif instruction.find("turn off") != -1:
        for row in range(start[0], end[0] + 1):
            for col in range(start[1], end[1] + 1):
                if grid[row, col] == 1:
                    grid[row, col] = 0
    elif instruction.find("toggle") != -1:
        for row in range(start[0], end[0] + 1):
            for col in range(start[1], end[1] + 1):
                if grid[row, col] == 1:
                    grid[row, col] = 0
                elif grid[row, col] == 0:
                    grid[row, col] = 1

print(f"Number of lights lit: {np.count_nonzero(grid)}")

# %%
grid = np.zeros([1000, 1000])
for index, instruction in enumerate(input):
    for k, c in enumerate(instruction):
        if c.isdigit():
            first_num = k
            break

    coords = instruction[first_num:].split(" through ")
    start_x = int(coords[0].split(",")[0])
    start_y = int(coords[0].split(",")[1])
    start = [start_x, start_y]
    end_x = int(coords[1].split(",")[0])
    end_y = int(coords[1].split(",")[1])
    end = [end_x, end_y]

    if instruction.find("turn on") != -1:
        for row in range(start[0], end[0] + 1):
            for col in range(start[1], end[1] + 1):
                grid[row, col] += 1
    elif instruction.find("turn off") != -1:
        for row in range(start[0], end[0] + 1):
            for col in range(start[1], end[1] + 1):
                if grid[row, col] > 0:
                    grid[row, col] -= 1
    elif instruction.find("toggle") != -1:
        for row in range(start[0], end[0] + 1):
            for col in range(start[1], end[1] + 1):
                grid[row, col] += 2

print(f"Total brightness: {np.sum(grid)}")
