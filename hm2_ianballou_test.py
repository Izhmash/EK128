def letters(s):
    letterCount = []
    s = s.lower()  # Case does not matter
    for i in range(0, 26):  # Loop 0 - 25 representing 26 letters
        letterCount.append(s.count(chr(i + 97)))  # Count letters via ASCII
    return letterCount


def bar_print(L26, height):
    graph = ""
    maxNum = max(L26)
    # Scaling Setup
    scalingFactor = height / maxNum
    for k in range(0, len(L26)):
        L26[k] *= scalingFactor
    # Graph creation
    for x in range(0, maxNum + 1):
        temp = ""
        # Construct graph line-by-line
        for i in L26:
            if (i <= maxNum - x):
                temp += "  "
            else:
                temp += "* "
        temp += "\n"
        graph += temp
    # build final alphabet line
    alpha = ""
    for j in range(65, 91):
        alpha += chr(j)
        alpha += " "
    return graph + alpha


def dot(L1, L2):
    prod = 0
    for i in range(0, 3):
        prod += (L1[i] * L2[i])
    return prod


def cross(L1, L2):
    return (L1[1] * L2[2] - L1[2] * L2[1]) + \
            (L1[2] * L2[0] - L1[0] * L2[2]) + \
            (L1[0] * L2[1] - L1[1] * L2[0])


def flatten(L):
    flattened = L
    while True:
        done = True
        # Algorithm flattens only nested lists
        # Loop needed for same-level lists
        for i in range(0, len(flattened)):
            if isinstance(flattened[i], list):
                done = False
                flatten(flattened[i])
                temp = flattened[i]
                del flattened[i]
                for j in range(0, len(temp)):
                    flattened.insert(i + j, temp[j])
        if done is True:
            return flattened
    return flattened


print(letters("aaaaAAAAAAzz"))

# small selection of text with one instance of each lowercase letter
one_each_text = "".join([chr(i) for i in range(ord('a'), ord('a')+26)])
print("one_each_text is:", one_each_text)

# now repeat with both lower and upper case
lower_upper_text = one_each_text+one_each_text.upper()
print("\nlower_upper_text is:", lower_upper_text)

# construct a string of lower case text with a total of 1 a, 2 b's, 3 c's etc
ramp_text = ""
for i in range(26):
    ramp_text += (one_each_text[i:])

print(bar_print(letters(ramp_text), 25))

print(dot([1, 2, 3], [3, 2, 1]))
print(cross([2, 1, 0], [3, 4, 0]))
print(flatten([0, 1, [2, 3], 4]))
print([1, 2, [3, 4, [5, [6, 7, 8], [9, 10]], 11, [12, [13, 14], [15, 16]]]])
print(flatten([1, 2, [3, 4, [5, [6, 7, 8], [9, 10]], 11, [12, [13, 14], [15, 16]]]]))
