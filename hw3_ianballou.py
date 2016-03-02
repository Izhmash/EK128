def word_count(mytext):
    mytext = mytext.lower()
    words = dict()
    mytextspaced = "".join([c if c.isalpha() else " " for c in mytext])
    wordList = mytextspaced.split(" ")
    for i in wordList:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words
print(word_count("This is a a a a a a test"))


def analyze(count_dictionary):
    sortedByKey = sorted(count_dictionary, reverse=True)
    sortedByValues = sorted(count_dictionary.values(), reverse=True)
    mostFreq = []
    longest = []
    longerThan1Count = 0
    for i in range(0, len(sortedByKey)):
        if len(sortedByKey[i]) == len(sortedByKey[0]):
            longest.append(sortedByKey[i])
        if len(sortedByKey[i]) > 1:
            longerThan1Count += 1
        
        
    # print(sortedDictKey)
    # print(sortedDictValues)
analyze(word_count("This is a a a a a a(test!"))


# def top_words(count_dictionary):
