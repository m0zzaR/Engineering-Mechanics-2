import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

F0 = 1.34e-7                    # kg/s^2
Cs = 1.736e-4                   # kg/s
r0 = np.array([2.416e6, 0 ])    # m
Omega = 7.2722e-5               # rad/s
Re = 6437378                    # m

time = (0,172800)               # 0 to 2 days in seconds
dt = 1                          # 1 second

t_eval = np.arange(time[0], time[1], dt)

np.random.seed() 
parcels = 10
angles = np.linspace(0, 2 * np.pi, parcels, endpoint=False)
radii = np.sqrt(np.random.uniform(0, Re**2, parcels))
x_init = radii * np.cos(angles)
y_init = radii * np.sin(angles)
initial_conditions = []

for i in range(parcels):
    x0, y0 = x_init[i], y_init[i]
    vx0, vy0 = 0, 0  
    initial_conditions.append([x0, y0, vx0, vy0])

def SOEs(t, state):
    x, y, vx, vy = state
    deltaX = x - r0[0]
    deltaY = y - r0[1]

    Fx = -F0 * deltaX - Cs * vx + 2 * Omega * vy - Omega**2 * x
    Fy = -F0 * deltaY - Cs * vy - 2 * Omega * vx - Omega**2 * y
    return [vx, vy, Fx, Fy]

trajectories = []

for ic in initial_conditions:
    sol = solve_ivp(SOEs, time, ic, t_eval=t_eval, method='RK45', max_step=1000)
    trajectories.append((sol.y[0], sol.y[1]))


plt.figure(figsize=(10, 10))
theta = np.linspace(0, 2 * np.pi, 200)
x_circle = Re * np.cos(theta)
y_circle = Re * np.sin(theta)
plt.plot(x_circle, y_circle, 'k--', label='Earth Boundary')

plt.plot(r0[0], r0[1], 'ro', label='Low-Pressure Center')

for x_traj, y_traj in trajectories:
    plt.plot(x_traj, y_traj)

plt.xlabel('X Position (miles)')
plt.ylabel('Y Position (miles)')
plt.title('Air Parcel Trajectories')
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
