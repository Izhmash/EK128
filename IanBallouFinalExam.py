import random
import numpy as np
from matplotlib import pyplot as plt
import cmath

student_email = "iballou@bu.edu"
student_id = "U11790741"
student_name = "Ian Ballou"


def report(transactions):
    income = 0
    expenses = 0
    for i in transactions:
        if i > 0:
            income += i
        else:
            expenses += i
    return [income, expenses]

#print("report output: ", report([-5, 6.7, 3.3, 6.9, 3.1, -3.3, 7.9, -.4, -1.3, 1.0]))


def get_digits(num, den):
    quo = divmod(num, den)[0]
    rem = divmod(num, den)[1]
    quos = []
    rems = []
    quos.append(quo)
    rems.append(rem)
    repeat = False
    while not repeat:
        #print("rep")
        remOld = rem
        quo = divmod(10*remOld, den)[0]
        rem = divmod(10*remOld, den)[1]
        quos.append(quo)
        rems.append(rem)
        if rems.count(rem) > 1:
            #print(rem, rems.count(rem))
            repeat = True
            repeatedNum = rem
    notRep = []
    for i in range(0, quos.index(repeatedNum) - 1):
        notRep.append(quos[i])
    rep = []
    for j in range(quos.index(repeatedNum), len(quos)):
        rep.append(quos[j])
    print(quos)
    return (notRep, rep)
#print("get_digits output: ", get_digits(1, 3)) # not totally working


def perfect_shuffle(deck):
    if len(deck) < 2:
        return deck
    half = len(deck)//2 + 1
    end = len(deck)
    front = deck[0:half]
    back = deck[half:end]
    #print(front, back)
    finalDeck = []
    select = True
    addOn = 0
    if len(back) > len(front):
        finalDeck.append(back[0])
        back.pop(0)
        addOn = 1
    for i in range(0 + addOn, end):
        if select:
            finalDeck.append(front[0])
            front.pop(0)
        else: 
            finalDeck.append(back[0])
            back.pop(0)
        select = not select
    return finalDeck

#print(perfect_shuffle([1]))
#print(perfect_shuffle([1,2,3,4,'A','B','C']))

#print("!!!Start prob 4!!!")
'''x=10
def myfun(x):
    x=2*x+3
    return x
print(x)
print(myfun(x))
print(x)'''


Variable_Scope = dict()

Variable_Scope['A'] = """Three values: 10, 23, 10"""
Variable_Scope['B'] = """1: x refers to an integer variable that is taking the value of 10.  2: x is a variable that is taken into myfun(x) as an argument.  It must be defined by the user.  3: x is the argument that the user inputs, now being multiplied by 2 times the input of myfun(x) and incremented by 3. 4: x is being returned by myfun(x) as (2*itself + 3)"""
Variable_Scope['C'] = """The first 10 comes from the inital declaration of x above. The rest of the x's are only within the scope of myfun.  The 23 is what is returned from myfun(x).  It is computed solely in myfun.  The last 10 is exactly the same as the first 10 because the x within the outermost scope is never reassigned before the final print call. """


def mytax(income):
    if income < 10000:
        return income * .05
    elif income < 20000:
        return 10000*.05 + (income-10000)*.1
    else:
        return 10000*.05 + (10000)*.1 + (income-20000)*.2
#print(mytax(24000))


def qroots(a, b, c):
    u=-b/(2*a)
    v=cmath.sqrt(b**2-4*a*c)/2*a
    return (u+v, u-v)
#print(qroots(1, 2, 10))


def generate(subjects, verbs, objects):
    final = []
    finalStr = ''
    for i in subjects:
        for j in verbs:
            for k in subjects:
                final.append([i, ' ', j, ' ', k])
    return final

# print(generate(['Professor Giles','He','She'],['ate','ran over','is'],['a cat', 'a sandwich']))

#D, T_current
def one_step(C,X):
      L = len(X)
      if L < 3:
          return
      T_nextStep = np.empty(L)
      # Slicing method to compute next step
      delta0 = X[1:] - X[:-1]
      result = np.zeros(L)
      result[:-1] += delta0
      result[1:] -= delta0
      T_nextStep = X+(-C*result)
      return T_nextStep
# print(one_step(.2, np.array([0, .2, .4, .5, .4 ,.2, 0])))
