f = open("Day2.txt")
input = f.read()
f.close()

up = input.count("(")
down = input.count(")")

print(f"up: {up}, down: {down}")
print(f"Santa ends up on floor {up - down}")

floor = 0
for i in range(len(input)):
    if input[i] == "(":
        floor += 1
    else:
        floor -= 1

    if floor < 0:
        print(f"Santa reached the basement at position {i + 1}")
        break
