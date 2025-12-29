f = open("Day5.txt")
input = f.read()
f.close()

# %%
input = input.splitlines()

# %%
vowels = "aeiou"
no_go = ["ab", "cd", "pq", "xy"]
nice_list = []
for i in range(len(input)):
    string = input[i]
    check_vowels = 0
    check_no_go = 1
    check_repeat = 0

    sum_vowels = sum([string.count(vowel) for vowel in vowels])
    if sum_vowels >= 3:
        check_vowels = 1

    for k in range(1, len(string)):
        if string[k] == string[k - 1]:
            check_repeat = 1

    sum_no_go = sum([string.count(check) for check in no_go])
    if sum_no_go > 0:
        check_no_go = 0

    if check_vowels and check_repeat and check_no_go:
        nice_list.append(string)

print(f"Number of nice strings: {len(nice_list)}")

# %%
nice_list = []
nice_index = []
for i in range(len(input)):
    string = input[i]
    check_pair = 0
    check_repeat = 0

    for k in range(1, len(string)):
        # pair = str([string[k - 1], string[k]])
        pair = string[k - 1 : k + 1]

        if string.find(pair, k + 1) != -1:
            check_pair = 1

        if k >= 2:
            if string[k] == string[k - 2]:
                check_repeat = 1

    if check_pair and check_repeat:
        nice_list.append(string)
        nice_index.append(i)

print(f"Number of nice strings: {len(nice_list)}")
