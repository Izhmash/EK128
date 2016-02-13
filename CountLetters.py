def countLetters(s):
    letterCount = []
    s = s.lower()
    for i in range(0, 26):
        letterCount.append(s.count(chr(i + 97)))
    return letterCount
print(countLetters("aaaAAAbbbBBBcccCCC"))

def createLetterGraph(L26, height):

