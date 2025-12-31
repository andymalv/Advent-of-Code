f = open("Day7.txt")
input = f.read().splitlines()
f.close()

# %%
calcs = {}
for index, instruction in enumerate(input):
    (into, out) = instruction.split("->")
    into = into.strip().split(" ")
    out = out.strip()
    calcs[out] = into

# %%
results = {}
for key, value in calcs.items():
    if len(value) == 1 and value[0].isdigit():
        results[key] = int(value[0])


def get_value(wire):
    if wire not in results.keys():
        input = calcs[wire]
        if len(input) == 1:
            output = get_value(input[0])
        else:
            operation = input[-2]
            if input[0].isdigit():
                first = int(input[0])
            elif input[0] == "NOT":
                pass
            else:
                first = get_value(input[0])
            if input[-1].isdigit():
                second = int(input[-1])
            else:
                second = get_value(input[-1])
            match operation:
                case "AND":
                    output = first & second
                case "OR":
                    output = first | second
                case "NOT":
                    output = ~second & 0xFFFF
                case "LSHIFT":
                    output = first << second
                case "RSHIFT":
                    output = first >> second

        results[wire] = output

    return results[wire]


print(f"Signal to wire a: {get_value('a')}")

# %%
results = {}
for key, value in calcs.items():
    if len(value) == 1 and value[0].isdigit():
        results[key] = int(value[0])

results["b"] = 16076

print(f"Signal to wire a, part 2: {get_value('a')}")
