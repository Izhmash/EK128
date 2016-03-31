import numpy as np
import matplotlib.pyplot as plt

student_email = "lina8589@bu.edu"
student_id  = "U81588389"
student_name = "Lina Lin Wei"


#Promblem 1
def single_step(D,T_current):
    L = len(T_current)
    if L < 3: #
        return
    next_T = np.empty(L)
    next_T[0] = T_current[0]+(D*(T_current[1]-T_current[0]))
    next_T[L-1] = T_current[L-1]+(D*(T_current[L-2]-T_current[L-1]))
    deltaT = (T_current[1:]- T_current[:-1])
    result = np.zeros(L)
    result[:-1] += deltaT
    result[1:] -= deltaT
    next_T = T_current +(D*result)
    return (next_T)
#temps = np.array([0,1,4,9,16,25,36,49,64,81,100])
#print(single_step(0.1, temps))

#start01=np.linspace(0,10,11)**2   
#next01=single_step(0.1,start01)
#print('start01\n',start01,'\nnext01\n',next01)


#Promblem 2
def stats(T):
    Average = np.average(T)
    StDev = np.std(T)
    return tuple([Average,StDev])
    
print(stats(temps))

#Problem 3
#L = 51
#a = np.zeros(L)
#a[25] = 100

def simulator(A):
    new_T = np.empty(1000) 
    for i in range(len(new_T)):
        X = single_step(0.02,A)
        Y = stats(X)
        new_T[i] = Y[1]
        A= X           
    return(new_T, plt.plot(new_T,'go'))

#print(simulator(a))
