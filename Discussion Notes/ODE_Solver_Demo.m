%% ODE Solver Demo (Simple Pendulum)

clear; clc; close all

% Parameters
g = 9.81; % acceleration due to gravity (m/s^2)
L = 1.0;  % length of the pendulum (m)

% Initial conditions
theta0 = pi/4;  % initial angular displacement (radians)
omega0 = 0;     % initial angular velocity (rad/s)
y0 = [theta0; omega0]; % initial state vector

% Time span for the simulation
tspan = [0 10]; % time range for the solution (seconds)

%% Method 1

% Define the system of ODEs as a function
pendulumODEs = @(t, y) [y(2); -g/L * sin(y(1))];

% Solve the ODE using ode45
[t, y] = ode45(pendulumODEs, tspan, y0);

% Plot the results
figure;
plot(t, y(:,1), '-r', 'LineWidth', 2); % plot theta (angular displacement)
hold on;
plot(t, y(:,2), '-b', 'LineWidth', 2); % plot omega (angular velocity)
xlabel('Time (s)');
ylabel('State variables');
legend('\theta (rad)', '\omega (rad/s)');
title('Simple Pendulum using ODE45');
grid on;


%% Method 2

% Solve the ODE using ode45
[t, y] = ode45(@pendulumODE, tspan, y0, [], g, L);

% Plot the results
figure;
plot(t, y(:,1), '-r', 'LineWidth', 2); % plot theta (angular displacement)
hold on;
plot(t, y(:,2), '-b', 'LineWidth', 2); % plot omega (angular velocity)
xlabel('Time (s)');
ylabel('State variables');
legend('\theta (rad)', '\omega (rad/s)');
title('Simple Pendulum using ODE45');
grid on;

% This function defines the ODEs for the simple pendulum.

function dydt = pendulumODE(t, y, g, L)
    % y(1) is theta (angular displacement)
    % y(2) is omega (angular velocity)
    
    dydt = zeros(2, 1);    % Initialize the output as a column vector
    
    dydt(1) = y(2);              % dy1/dt = omega
    dydt(2) = -g/L * sin(y(1));  % dy2/dt = -g/L * sin(theta)
end