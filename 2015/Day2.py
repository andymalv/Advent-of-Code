f = open("Day2.txt")
input = f.read()
f.close()

boxes = []
mark = 0
for i in range(len(input)):
    if input[i] == "\n":
        boxes.append(input[mark:i])
        mark = i + 1

paper_total = 0
ribbon_total = 0
for i in range(len(boxes)):
    box = boxes[i]
    xs = [index for index, letter in enumerate(box) if letter == "x"]
    length = int(box[0 : xs[0]])
    width = int(box[xs[0] + 1 : xs[1]])
    height = int(box[xs[1] + 1 :])
    dims = [length, width, height]
    dims.sort()

    surface_area = (2 * length * width) + (2 * width * height) + (2 * height * length)
    extra = dims[0] * dims[1]
    paper = surface_area + extra
    paper_total = paper + paper_total

    ribbon = (2 * dims[0]) + (2 * dims[1])
    bow = length * width * height
    ribbon_total = ribbon + bow + ribbon_total

print(f"Total wrapping paper: {paper_total}")
print(f"Total ribbon: {ribbon_total}")

# %%
