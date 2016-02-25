import math

student_email = "iballou@bu.edu"
student_id = "U11790741"
student_name = "Ian Ballou"

COMMENT = dict()


def nextC(N):
    if (N % 2 == 0):
        return N//2
    else:
        return (3 * N) + 1


def coll(N):
    count = 0
    while (N != 1):
        N = nextC(N)
        count += 1
    return count


def partition(L, p):
    lessThanList = []
    equalCount = 0
    greaterThanList = []
    for i in range(0, len(L)):
        if (L[i] < p):
            lessThanList.append(L[i])
        elif (L[i] > p):
            greaterThanList.append(L[i])
        else:
            equalCount += 1
    return(lessThanList, equalCount, greaterThanList)


def polar_difference(P, Q):
    rP = P[0]
    thetaP = P[1]
    rQ = Q[0]
    thetaQ = Q[1]
    thetaDiff = thetaP - thetaQ
    xP = rP*math.cos(thetaP)
    yP = rP*math.sin(thetaP)
    xQ = rQ*math.cos(thetaQ)
    yQ = rQ*math.sin(thetaQ)
    rDiff = math.sqrt((xP - xQ)**2 + (yP - yQ)**2)
    return (thetaDiff, rDiff)

# print(polar_difference((1, 0), (2, 0)))


def order3(one, two, three):
    return sorted([one, two, three])

COMMENT['explanation'] = """This program loops through the string and then through
                            a list containing the vowels.  Checks if there is a vowel
                            and shifts that vowel by one"""

def vowel_shift(S):
    shifted = []
    for i in range(0, len(S)):
        shifted.append(S[i])
    print(shifted)
    vowelsL = ['a', 'e', 'i', 'o', 'u']
    vowelsU = ['A', 'E', 'I', 'O', 'U']
    for j in range(0, len(shifted)):
        for k in range(0, len(vowelsL)):
                if (shifted[j] == vowelsL[k]):
                    if (shifted[j] == "u"):
                        shifted[j] = "a"
                    else:
                        shifted[j] = vowelsL[k + 1]
                if (shifted[j] == vowelsU[k]):
                    if (shifted[j] == "U"):
                        shifted[j] = "A"
                    else:
                        shifted[j] = vowelsU[k + 1]
    shifted = str(shifted)
    return shifted
