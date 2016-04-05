import math
import numpy as np
from matplotlib import pyplot as plt
from scipy.integrate import odeint


# y: [theta, omega], t: times, D: damping, D2: drag
def pendulum_rate2(y, t, D, D2):
    theta = y[0]
    omega = y[1]
    return [omega, -math.sin(theta) - D*omega - D2 * omega*abs(omega)]


max_time = 80
num_points = 200
times_2 = np.linspace(0, max_time, num_points)  # base time data array

D_value = 0.1  # damping coefficient
D2_value = 0.02

# run and plot the simulation
omega0 = 2.0  # initial angular velocity (will assume initial angle = 0)

p = odeint(pendulum_rate2, [0, omega0], times_2, (D_value, D2_value))

# just plot the results right away
plt.figure(figsize=(10, 12))

plt.subplot(2, 1, 1)  # two plots above one another, top one now
plt.xlabel('t', fontsize=14)
plt.title('Theta for D={:.3f}, D2={:.3f}, N={} omega={}'.format(D_value,
                                                                D2_value,
                                                                len(times_2),
                                                                omega0),
          fontsize=14,
          color='blue')
plt.plot(times_2, p[:, 0], 'b-')

plt.subplot(2, 1, 2)  # lower plot
plt.title('Omega', fontsize=14, color='red')
plt.xlabel('t', fontsize=14)
plt.plot(times_2, p[:, 1], 'r-')

plt.show()

# Helpful for energy? e=0.5*p[:,1]**2+1-np.cos(p[:,0])
