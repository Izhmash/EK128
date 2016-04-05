import numpy as np
from matplotlib import pyplot as plt

student_email = "iballou@bu.edu"
student_id = "U11790741"
student_name = "Ian Ballou"


def summarize(data):
    costs = dict()
    for i in data:
        if i[0] in costs:
            costs[i[0]] += i[1]
        else:
            costs[i[0]] = i[1]
    return costs


def final_score(alpha, original, new):
    scores = np.empty(len(original))
    trues = original > (alpha * new + (1-alpha) * original)
    for i in range(0, len(original)):
        if trues[i] == True:
            scores[i] = original[i]
        else:
            scores[i] = (alpha * new[i] + (1-alpha) * original[i])
    return scores


def plot_scores(original, final):
    plt.plot(original, 'bx')
    plt.plot(final, 'ro')
    plt.show()
