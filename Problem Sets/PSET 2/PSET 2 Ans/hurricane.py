import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
F0 = 1000            # kg/day^2
cs = 15              # kg/day
Omega = 2 * np.pi    # radians/day
R_earth = 4000       # miles
r0 = np.array([1500, 0])  # Low-pressure center position (miles)

# Time span
t_span = (0, 2)      # Simulate for 2 days
dt = 0.01            # Time step in days
t_eval = np.arange(t_span[0], t_span[1], dt)

# Initial positions of air parcels
np.random.seed(0)  # For reproducibility
num_parcels = 10
angles = np.linspace(0, 2 * np.pi, num_parcels, endpoint=False)
radii = np.sqrt(np.random.uniform(0, R_earth**2, num_parcels))
x_init = radii * np.cos(angles)
y_init = radii * np.sin(angles)
initial_conditions = []

for i in range(num_parcels):
    x0, y0 = x_init[i], y_init[i]
    vx0, vy0 = 0, 0  # Initial velocities in rotating frame
    initial_conditions.append([x0, y0, vx0, vy0])

# Equations of motion
def equations(t, state):
    x, y, vx, vy = state
    rx, ry = x - r0[0], y - r0[1]
    # Forces
    Fx = -F0 * rx - cs * vx + 2 * Omega * vy - Omega**2 * x
    Fy = -F0 * ry - cs * vy - 2 * Omega * vx - Omega**2 * y
    return [vx, vy, Fx, Fy]

# Solve ODEs for each air parcel
trajectories = []

for ic in initial_conditions:
    sol = solve_ivp(equations, t_span, ic, t_eval=t_eval, method='RK45')
    trajectories.append((sol.y[0], sol.y[1]))

# Plotting
plt.figure(figsize=(10, 10))
theta = np.linspace(0, 2 * np.pi, 200)
x_circle = R_earth * np.cos(theta)
y_circle = R_earth * np.sin(theta)
plt.plot(x_circle, y_circle, 'k--', label='Earth Boundary')

# Plot low-pressure center
plt.plot(r0[0], r0[1], 'ro', label='Low-Pressure Center')

# Plot trajectories
for x_traj, y_traj in trajectories:
    plt.plot(x_traj, y_traj)

plt.xlabel('X Position (miles)')
plt.ylabel('Y Position (miles)')
plt.title('Air Parcel Trajectories')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
