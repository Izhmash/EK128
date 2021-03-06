student_email = "iballou@bu.edu"
student_id = "U11790741"
student_name = "Ian Ballou"


def word_count(mytext):
    mytext = mytext.lower()
    words = dict()
    # This line replaces all non-letters with spaces
    mytextspaced = ''.join([c if c.isalpha() else " " for c in mytext])
    wordList = mytextspaced.split()
    # Count words
    for i in wordList:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words


def analyze(count_dictionary):
    sortedByKey = sorted(count_dictionary, key=len, reverse=True)
    mostFreq = []
    longest = []
    longerThan1Count = 0
    # Populate longest word list and count the words longer than one
    for i in range(0, len(sortedByKey)):
        if len(sortedByKey[i]) == len(sortedByKey[0]):
            longest.append(sortedByKey[i])
        if len(sortedByKey[i]) > 1:
            longerThan1Count += 1
    largestFreq = count_dictionary[max(count_dictionary, key=count_dictionary.get)]
    # Populate the list of the most frequent words
    for j, k in count_dictionary.items():
        if k == largestFreq:
            mostFreq.append(j)
    return longerThan1Count, set(mostFreq), set(longest)


def top_words(count_dictionary, n):
    mostNFreq = []
    countDictSet = set(count_dictionary.values())
    # A sorted list of all frequencies with no duplicates
    sortedByFreqSet = list(sorted(countDictSet, reverse=True))
    # Loops thru words and freqs. list, checks for freqs. of diff populations
    count = 0
    while n > count:
        for i, j in count_dictionary.items():
            if j == sortedByFreqSet[count]:
                mostNFreq.append(tuple([i, j]))
        count += 1
    return mostNFreq

