import hashlib

input = "yzbqklnj"

# %%
i = 0
five_zeros = 0

while True:
    data = input + str(i)
    hash = hashlib.md5(data.encode()).hexdigest()

    if not five_zeros and hash.startswith("00000"):
        five_zeros = i

    if five_zeros:
        break

    i += 1

print(f"Five zero answer: {five_zeros}")

# %%
i = 0
six_zeros = 0

while True:
    data = input + str(i)
    hash = hashlib.md5(data.encode()).hexdigest()

    if not six_zeros and hash.startswith("000000"):
        six_zeros = i

    if six_zeros:
        break

    i += 1

print(f"Six zero answer: {six_zeros}")
