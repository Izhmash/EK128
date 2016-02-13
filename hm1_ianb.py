student_email = "iballou@bu.edu"
student_id = "U11790741"
student_name = "Ian Ballou"


def dashify(x):
    for i in range(1, len(x) + (len(x) - 1), 2):  # compensate for growing str
        x = x[:i] + "-" + x[(i):]  # put "-" between chars at i and i + 1
    print(x)
# dashify("123456")


def isHappy(h):
    numStr = str(h)
    if (h < 1):  # Number cannot be less than 1
        return(False)
    while(int(numStr) != 1):
        if (int(numStr) == 4):  # check for 4: indicates unhappy number
                return False
        temp = 0
        for i in range(0, len(numStr)):  # sum squares of digits
            temp += int(numStr[i])**2
        numStr = str(temp)  # store result for rechecking
    return True
print(isHappy(836))


def isPerfect(p):
    temp = 0
    for i in range(1, p):
        if (p % i == 0):  # check for factor
            temp += i  # Add factor to growing sum
    if (temp == p):
        return True
    else:
        return False
# print(isPerfect(496))


def pyramid(s):
    for i in range(0, s):  # Loop for enters
        for j in range(0, s - i):  # Loop for spaces
            print(" ", end="")
        for k in range(0, i * 2 + 1):  # Loop for stars
            print("*", end="")
        print()
# pyramid(5)
