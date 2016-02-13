def countLetters(s):
    letterCount = []
    s = s.lower()
    for i in range(0, 26):
        letterCount.append(s.count(chr(i + 97)))
    return letterCount
print(countLetters("aaaaAAAAAAzz"))


def getLetterGraph(L26, height):
    # TODO: Scaling algorithm
    graph = ""
    maxNum = max(L26)
    scalingFactor = height / maxNum
    print(scalingFactor)
    for k in range(0, len(L26)):
        L26[k] *= scalingFactor
    print(L26)
    for x in range(0, maxNum + 1):  # maxNum should get replaced by height?
        temp = ""
        for i in L26:
            if (i <= maxNum - x):
                temp += "  "
            else:
                temp += "* "
        temp += "\n"
        graph += temp
    return graph


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

# print(getLetterGraph(countLetters(ramp_text), 5))
print(getLetterGraph(countLetters("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaccccccaaazzz"), 10))
