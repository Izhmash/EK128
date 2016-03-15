def word_count(mytext):
    mytext = mytext.lower()
    words = dict()
    mytextspaced = "".join([c if c.isalpha() else " " for c in mytext])
    wordList = mytextspaced.split()
    for i in wordList:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words
print(word_count("This is is is is is is is a(test"))


def analyze(count_dictionary):
    sortedByKey = sorted(count_dictionary, key=len, reverse=True)
    mostFreq = []
    longest = []
    longerThan1Count = 0
    for i in range(0, len(sortedByKey)):
        if len(sortedByKey[i]) == len(sortedByKey[0]):
            longest.append(sortedByKey[i])
        if len(sortedByKey[i]) > 1:
            longerThan1Count += 1
    largestFreq = count_dictionary[max(count_dictionary, key=count_dictionary.get)]
    for j, k in count_dictionary.items():
        if k == largestFreq:
            mostFreq.append(j)
    return longerThan1Count, set(mostFreq), set(longest)
print(analyze(word_count("This is y y y y y y a a a a a a(test! Imaginary people woah creaTions")))


def top_words(count_dictionary, n):
    mostNFreq = []
    countDictSet = set(count_dictionary.values())
    sortedByFreqSet = list(sorted(countDictSet, reverse=True))
    count = 0
    while n > count:
        for i, j in count_dictionary.items():
            if j == sortedByFreqSet[count]:
                mostNFreq.append(tuple([i, j]))
        count += 1
    return mostNFreq

print(top_words(word_count(text), 4))
