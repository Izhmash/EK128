def testFunction(a):
    count = 0
    for i in a:
        if i == "x":
            count = count + 1
    return count

def secondTest(b):
    return (b * 2)

print(secondTest(testFunction("xyxyxy")))
