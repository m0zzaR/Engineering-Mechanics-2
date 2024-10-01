import numpy as np
import matplotlib.pyplot as plt

# Magnitude of Initial Velocity (m/s)
v0 = 10

# Mass of sparkles (converted to kilograms)
ms = 10/1000

# Gravity (m/s^2)
g = -9.81

# Drag Coef (N s/m)
cs1 = 0.001 
cs2 = 0.01

# Force of Drag (N)
Fdrag = [cs1 * v0, cs2 * v0]

# Total Sim Time (s)
t_final = 1.5
dt = 0.01 # Time step (s)
t = np.arange(0, t_final + dt, dt) # Time Array

# Angles of each spark (degrees)
angles = np.linspace(20, 160, 8)  # Eight angles in the vertical plane
angles_rad = np.radians(angles)  # Convert angles to radians

# Function to compute drag force
def compute_drag(vx, vy, cs):
    v = np.sqrt(vx**2 + vy**2)  # Magnitude of velocity
    Fdrag_x = -cs * v * vx  # Drag in x-direction
    Fdrag_y = -cs * v * vy  # Drag in y-direction
    return Fdrag_x, Fdrag_y

# Simulate motion of sparks with a given drag coef
def sim_sparks(cs, angles_rad):
    traj_x = []
    traj_y = []

    for theta in angles_rad:
        # Initialize velocities
        vx = v0 * np.cos(theta)
        vy = v0 * np.sin(theta)

        # Initialize positions
        x = 0
        y = 0

        x_traj = [x]
        y_traj = [y]

        # Time step loop
        for _ in t:
            # Compute Drag forces
            Fdrag_x, Fdrag_y  = compute_drag(vx, vy, cs)

            # Compute accelerations
            ax = Fdrag_x / ms
            ay = (Fdrag_y / ms) + g

            # Update Velocities
            vx += ax * dt
            vy += ay * dt

            # Update positions
            x += vx * dt
            y += vy * dt

            # Append positions to trajectory lists
            x_traj.append(x)
            y_traj.append(y)

        # Store trajectories for all sparks
        traj_x.append(x_traj)
        traj_y.append(y_traj)

    return traj_x, traj_y


# Simulate for both drag coef
x1, y1 = sim_sparks(cs1, angles_rad)
x2, y2 = sim_sparks(cs2, angles_rad)

# Plot the results for both drag coef
plt.figure(figsize = (10,6))

# Plot for cs1
for i in range(8):
    plt.plot(x1[i], y1[i], label=f'Drag cs={cs1} (spark {i+1})')

for i in range(8):
    plt.plot(x2[i], y2[i], '--', label=f'Drag cs={cs2} (spark {i+1})', alpha=0.7)

plt.title('Trajectories of Firework Sparks with Different Drag Coefficients')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.legend(loc='upper right', fontsize='7', ncol=2)
plt.grid(True)
plt.xlim(-10, 10)  # Set the x-axis limits (in meters, adjust as necessary)
plt.ylim(-6, 6)  # Set the y-axis limits (in meters, adjust as necessary)
plt.show()

