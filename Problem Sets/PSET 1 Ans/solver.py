import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
g = 9.81  # acceleration due to gravity (m/s^2)
L = 1.0   # length of the pendulum (m)

# Initial conditions
theta0 = np.pi / 4  # initial angular displacement (radians)
omega0 = 0          # initial angular velocity (rad/s)
y0 = [theta0, omega0]  # initial state vector

# Time span for the simulation
tspan = np.linspace(0, 10, 250)  # time range for the solution (seconds)

# Define the system of ODEs as a function
def pendulum_ODEs(y, t, g, L):
    theta, omega = y
    dydt = [omega, -g / L * np.sin(theta)]
    return dydt

# Solve the ODE using odeint (Method 1)
solution = odeint(pendulum_ODEs, y0, tspan, args=(g, L))

# Extracting the theta and omega (angular velocity) from the solution
theta = solution[:, 0]
omega = solution[:, 1]

# Plot the results (Method 1)
plt.figure()
plt.plot(tspan, theta, '-r', linewidth=2, label=r'$\theta$ (rad)')
plt.plot(tspan, omega, '-b', linewidth=2, label=r'$\omega$ (rad/s)')
plt.xlabel('Time (s)')
plt.ylabel('State variables')
plt.legend()
plt.title('Simple Pendulum using ODE Solver (odeint)')
plt.grid(True)
plt.show()

# Define another function for Method 2 (same as the first)
def pendulum_ODE(t, y, g, L):
    dydt = np.zeros(2)
    dydt[0] = y[1]    # dy1/dt = omega
    dydt[1] = -g / L * np.sin(y[0])  # dy2/dt = -g/L * sin(theta)
    return dydt

# Solve the ODE using odeint (Method 2)
solution2 = odeint(pendulum_ODE, y0, tspan, args=(g, L))

# Extracting the theta and omega from the solution (Method 2)
theta2 = solution2[:, 0]
omega2 = solution2[:, 1]

# Plot the results (Method 2)
plt.figure()
plt.plot(tspan, theta2, '-r', linewidth=2, label=r'$\theta$ (rad)')
plt.plot(tspan, omega2, '-b', linewidth=2, label=r'$\omega$ (rad/s)')
plt.xlabel('Time (s)')
plt.ylabel('State variables')
plt.legend()
plt.title('Simple Pendulum using ODE Solver (Method 2)')
plt.grid(True)
plt.show()
