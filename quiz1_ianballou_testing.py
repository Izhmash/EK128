student_email = "iballou@bu.edu"
student_id = "U11790741"
student_name = "Ian Ballou"

import numpy as np
from matplotlib import pyplot as plt


def summarize(data):
    costs = dict()
    for i in data:
        if i[0] in costs:
            costs[i[0]] += i[1]
        else:
            costs[i[0]] = i[1]
    return costs


d = [['Fatimah', 19.82], ['Naelle', 36.31], ['Olivia', 38.41], ['Li', 14.06], 
   ['Anthony', 46.23], ['Fatimah', 48.22], ['Anthony', 21.59], ['Fatimah', 19.26], 
   ['Anthony', 46.35], ['Chuong', 38.85], ['Joaquin', 34.59], ['Anthony', 17.92], 
   ['Anthony', 12.53], ['Li', 25.46], ['Naelle', 15.40]]

print(summarize(d))


def final_score(alpha, original, new):
    scores = np.empty(len(original))
    trues = original > (alpha * new + (1-alpha) * original)
    for i in range(0, len(original)):
        if trues[i] == True:
            scores[i] = original[i]
        else:
            scores[i] = (alpha * new[i] + (1-alpha) * original[i])
    return scores

original = np.array([ 38.,  24.,  70.,  42.,  77.,  48.,   44.,   48.,   46.,  28.])
new = np.array([ 64.,  54.,  47.,  62.,  49.,  61.,   94.,   69.,   66.,  44.])

print(final_score(0.25, original, new))


def plot_scores(original, final):
    plt.plot(original, 'bx')
    plt.plot(final, 'ro')
    plt.show()

plot_scores(original, final_score(0.25, original, new))
