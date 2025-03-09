import numpy as np
import matplotlib.pyplot as plt
from euler_method import EulerMethod

def temperature_sine(t):
    return 5.05953 * np.sin(0.267757 * t - 2.33298) + 33.42659

hours = np.arange(24)
outdoor_temps = np.array([29.4, 29.4, 28.9, 28.3, 28.3, 28.3, 28.9, 31.1, 32.8,
                         34.4, 35.6, 36.1, 37.8, 37.8, 38.9, 38.9, 37.8, 37.2,
                         36.1, 34.4, 33.3, 32.8, 32.2, 31.7])

# Parameters
t_start = 0      # Start time (hours)
t_end = 24      # End time (hours, 7 days)
dt = 0.1         # Time step (hours)
T0 = 29.4     # Initial indoor temperature (Celsius)
M = 216.22       # Mass of air (kg)
c = 1.005       # Specific heat of air (kJ/kg·K)
k_fiber = 0.3         # Thermal conductivity
s_fiber = 0.4          # Thickness
A_fiber = 84.15         # Surface area (m**2)
k_glass =  5.7       # Thermal conductivity
s_glass = 0.002381        # Thickness
A_glass = 0.464515         # Surface area (m**2)

euler = EulerMethod(t_start, t_end, dt, T0, M, c, k_fiber, s_fiber, A_fiber, k_glass, s_glass, A_glass, temperature_sine)
t, T = euler.solve()

plt.figure(figsize=(12, 6))
plt.plot(t, T, label='Indoor Temperature')
plt.plot(hours, outdoor_temps, 'r.', label='Outdoor Temperature (Data Points)')
t_continuous = np.linspace(0, t_end, 1000)
plt.plot(t_continuous, [temperature_sine(ti % 24) for ti in t_continuous], 'r--',
         alpha=0.5, label='Outdoor Temperature (Sine Fit)')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.title('Indoor vs Outdoor Temperature Over Time (House 2)')
plt.grid(True)
plt.legend()
plt.show()