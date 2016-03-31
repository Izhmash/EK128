import numpy as np
from matplotlib import pyplot as plt

student_email = "iballou@bu.edu"
student_id = "U11790741"
student_name = "Ian Ballou"


def single_step(D, T_current):
    L = len(T_current)
    if L < 3:
        return
    T_nextStep = np.empty(L)
    # Slicing method to compute next step
    delta0 = T_current[1:] - T_current[:-1]
    result = np.zeros(L)
    result[:-1] += delta0
    result[1:] -= delta0
    T_nextStep = T_current+D*result
    return T_nextStep


def stats(T):
    # Average = (sum of all T's)/L
    # StDev = sqrt(Average(T**2) - Average(T)**2)
    Average = np.average(T)
    StDev = np.std(T)
    return Average, StDev


# Prints a graph of the standard deviations with 300 steps
def simulation(D, a):
    devs = np.empty(300)
    devs[0] = stats(a)[1]
    for i in range(1, len(devs)):
        a = single_step(0.02, a)
        devs[i] = stats(a)[1]
    print(devs)
    plt.plot(devs, 'b-')
    plt.plot(devs, 'ro')
    plt.show()
