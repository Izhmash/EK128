import numpy as np
from matplotlib import pyplot as plt

student_email = "iballou@bu.edu"
student_id = "U11790741"
student_name = "Ian Ballou"

# Do with slicing instead?
"""def single_step(D, T_current):
    L = len(T_current)
    if L < 3:
        return
    T_nextStep = np.empty(len(T_current))
    T_nextStep[0] = T_current[0] + D*(T_current[1] - T_current[0])
    T_nextStep[L-1] = T_current[L-1] + D*(T_current[L-2] - T_current[L-1])
    for i in range(1, L - 1):
        delta = D*(T_current[i+1]-T_current[i])\
            + D*(T_current[i-1]-T_current[i])
        T_nextStep[i] = T_current[i] + delta
    return T_nextStep"""


def single_step(D, T_current):
    # print(T_current)
    L = len(T_current)
    if L < 3:
        return
    T_nextStep = np.empty(L)
    delta0 = T_current[1:] - T_current[:-1]
    # print(delta0)
    result = np.zeros(L)
    # print(result)
    result[:-1] += delta0
    # print(result)
    result[1:] -= delta0
    # print(result)
    T_nextStep = T_current+D*result
    return T_nextStep


# print(single_step(1, np.array([5, 7, 8, 4, 2, 1, 12, 10])))
"""ar = np.array([0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100])
arTest = np.zeros(51)
arTest[25] = 100
print(single_step(0.02, arTest))
'''for i in range(0, 100):
    arTest = single_step(.02, arTest)
    print(arTest)'''
"""


def stats(T):
    # Average = (sum of all T's)/L
    # StDev = sqrt(Average(T**2) - Average(T)**2)
    Average = np.average(T)
    StDev = np.std(T)
    return Average, StDev

"""print(stats(arTest))
devs = np.empty(1000)
devs[0] = stats(arTest)[1]
for i in range(1, len(devs)):
    arTest = single_step(0.02, arTest)
    devs[i] = stats(arTest)[1]
print(devs)
plt.plot(devs, 'b-')
plt.plot(devs, 'ro')
plt.show()"""


arTest = np.empty(51)
arTest[25] = 100

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
simulation(.02, arTest)
"""
# # HW4 Result Checker
# This notebook contains a checker for results from HW4.
# The notebook can be downloaded as a [python file](HW4_Result_Checker.py)
# 
# The following things are defined in this notebook:
# - An initial ndarray named TESTER_0 of size 30.
# - A array called TESTER_1 which is the result of a single time step with D=0.1:
# 
#         TESTER_T1=single_step(0.05,TESTER_0)
#     
# - A third array called TESTER_100 which is the result of 100 forward time steps starting from TESTER_0 with D=0.05.
# - A function 
# 
#         check_stepper(your_single_step_function)
#     
#     which you can call on the function single_step() you defined as the answer for part 1.  This check function runs your function for 1 and for 100 steps and compares the results to the arrays defined above.  It prints out the max deviation of your results for each array and also returns True if the deviations are smaller in than 1.0e-6 at each point.
#    

# In[1]:

# get_ipython().magic('matplotlib inline')


# In[2]:

# import numpy as np
# from matplotlib import pyplot as plt


# In[3]:

# SAMPLE DATA
TESTER_0=np.array([2.021083228643781315e-01,2.891667664034314189e-01,3.829932871898905633e-01,4.764026345912069638e-01,5.610569439564202510e-01,6.281102502072556382e-01,6.690555426268545158e-01,6.767559428151684875e-01,6.466219206026277977e-01,5.778663875203886580e-01,4.747213953556869148e-01,3.474246440460471708e-01,2.126750545293408234e-01,9.312527819304100563e-02,1.537929137763354055e-02,6.024528471328208581e-03,8.565568071277032680e-02,2.618090469246132090e-01,5.230581833447166540e-01,8.374151606005953985e-01,1.157407164921202547e+00,1.431288263303582164e+00,1.616321119070618595e+00,1.688680234050056184e+00,1.646540124052456200e+00,1.506618490025229740e+00,1.297067800548619365e+00,1.049951000513316135e+00,7.953568205248225942e-01,5.578052735076287627e-01,3.546908360705608998e-01,1.961755006138064805e-01,8.595571118379467801e-02,2.246892922805819939e-02,2.548026033755975230e-04,1.129884365684230736e-02,4.625984586653036912e-02,9.552632929841585463e-02,1.500734486921775079e-01,2.021083228643780205e-01])
TESTER_1=np.array([2.108141672182834714e-01,2.898435741281720213e-01,3.829515698513762945e-01,4.755271307875966746e-01,5.592968436449824443e-01,6.254994488241319983e-01,6.657310534037260696e-01,6.729725005750830658e-01,6.427597695156579416e-01,5.744274416121424309e-01,4.723062194411931092e-01,3.466793602253405160e-01,2.141950358473814764e-01,9.730565714513024489e-02,2.221841376854375577e-02,1.492311998610295481e-02,9.530790210981041066e-02,2.703186239454392625e-01,5.283689674282942006e-01,8.379786633070682722e-01,1.152796074327379738e+00,1.422403439042047912e+00,1.605053744991858711e+00,1.677230311552352360e+00,1.636761971649493663e+00,1.499655584480291459e+00,1.293311189492750035e+00,1.049203262517997004e+00,7.970610838219525096e-01,5.612489844656413096e-01,3.591507462685922247e-01,2.010050552164807380e-01,9.062901193122220589e-02,2.659619476116358711e-02,3.580619371190528998e-03,1.369053977246444294e-02,4.769039398875011410e-02,9.605439289460347696e-02,1.498222241700213897e-01,1.969048354471579776e-01])
TESTER_100=np.array([4.283790438976103898e-01,4.340320494720032451e-01,4.440499026931944426e-01,4.561017083788450055e-01,4.672624751710870439e-01,4.745893261511548999e-01,4.757306332250580416e-01,4.694701364429546553e-01,4.561181144278266264e-01,4.376812073568285277e-01,4.177686490091159777e-01,4.012242135296839041e-01,3.935096580256678966e-01,3.999051689164568324e-01,4.246307121696620279e-01,4.700214764860173866e-01,5.359014753305015866e-01,6.192841359537950563e-01,7.144847577400720295e-01,8.136619855652483801e-01,9.077264411688219514e-01,9.874818830571373551e-01,1.044815442024184415e+00,1.073741219564193772e+00,1.071129343721382465e+00,1.037013655141139967e+00,9.744505403369124741e-01,8.889804176182485307e-01,7.878051860709255338e-01,6.788288900066041798e-01,5.697123674959009287e-01,4.670705446995815358e-01,3.759026685157847436e-01,2.993014733021351903e-01,2.384453527041448806e-01,1.928428181368115335e-01,1.607723337672757324e-01,1.398426658122823851e-01,1.275887488982324069e-01,1.220163009443835933e-01])


# In[4]:

# graph the initial state
plt.plot(TESTER_0,'b.')


# In[5]:

# graph the small shift for the first state
# plt.plot(TESTER_1-TESTER_0,'g.')


# In[6]:

#compare step 100 to initial
#plt.plot(TESTER_0,'b.')
#plt.plot(TESTER_100,'r.')


# In[7]:

def check_stepper(f):
    '''runs f as a the single_step function for D=0.1 and initial state TESTER_0
    Prints status updates and returns true deviations at all points are less than 1.0e-6'''
    D_test=0.1
    Max_error=1.0e-6
    ok=True
    
    my_t0=TESTER_0.copy() # make a copy of the initial data in case f tries to modify it!
    print("Trying a single step...")
    my_t1=f(D_test,my_t0)
    if (np.any(my_t0 != TESTER_0)):
        print("    The step_function changed the initial array!  Sorry -- not allowed!")
        ok=False
    t1_deviation=np.max(np.abs(my_t1-TESTER_1))
    print('    The maximum deviation after 1 step was',t1_deviation)
    ok = ok and (t1_deviation<=Max_error)
    
    print('Trying 100 steps from the start...')
    my_t100=my_t0
    for i in range(100):
        my_t100=f(D_test,my_t100) # repeat 1 forward step
        
    t100_deviation=np.max(np.abs(my_t100-TESTER_100))
    print('    The maximum deviation after 100 steps was',t100_deviation)
    ok = ok and (t100_deviation<=Max_error)
    return ok



# In[ ]:


# check_stepper(single_step)
"""
