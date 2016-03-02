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
# print(word_count("This(is)a test.this.is.a.test THiS is-a-Test TeSting"))


def analyze(count_dictionary):
    return

# def top_words(count_dictionary):
