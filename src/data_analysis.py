
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
from cooling_model import cooling_model
from numerical_methods import euler_method, rk4_method

# Load experimental data
data = pd.read_csv("data/experimental_data.csv")

time = data["time"].values
temperature = data["temperature"].values

# Ambient temperature
Ts = 25

# Estimate initial temperature and cooling constant
parameters, covariance = curve_fit(
    lambda t, T0, k: cooling_model(t, T0, Ts, k),
    time,
    temperature,
    p0=[75, 0.05]
)

T0, k = parameters

# Simulation settings
dt = 0.1
total_time = max(time)

# Analytical solution
t_analytical = np.arange(0, total_time + dt, dt)
T_analytical = cooling_model(
    t_analytical, T0, Ts, k
)

# Euler method
t_euler, T_euler = euler_method(
    T0, Ts, k, dt, total_time
)

# Runge-Kutta method
t_rk4, T_rk4 = rk4_method(
    T0, Ts, k, dt, total_time
)

# Plot comparison
plt.figure(figsize=(10, 6))

plt.scatter(
    time, temperature,
    label="Experimental Data"
)

plt.plot(
    t_analytical, T_analytical,
    label="Analytical Solution"
)

plt.plot(
    t_euler, T_euler,
    "--",
    label="Euler Method"
)

plt.plot(
    t_rk4, T_rk4,
    ":",
    linewidth=2,
    label="Runge-Kutta 4"
)

plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Comparison of Cooling Models")

plt.legend()
plt.grid()

plt.savefig("plots/method_comparison.png", dpi=300)
plt.show()

print("Initial Temperature:", round(T0, 3))
print("Cooling Constant:", round(k, 5))
print("Ambient Temperature:", Ts)
