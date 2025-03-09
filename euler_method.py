import numpy as np

class EulerMethod:
    """Class to solve the temperature differential equation using Euler's method."""

    def __init__(self, t_start, t_end, dt, T0, M, c, k_fiber, s_fiber, A_fiber, k_glass, s_glass, A_glass, temp_func):
        """Initialize the Euler method solver for temperature differential equations.

        Args:
            t_start (float): Start time in hours.
            t_end (float): End time in hours.
            dt (float): Time step in hours.
            T0 (float): Initial indoor temperature in Celsius.
            M (float): Mass of air in kg.
            c (float): Specific heat of air in kJ/kg·K.
            k_fiber (float): Thermal conductivity of fiber material.
            s_fiber (float): Thickness of fiber material in meters.
            A_fiber (float): Surface area of fiber material in m².
            k_glass (float): Thermal conductivity of glass material.
            s_glass (float): Thickness of glass in meters.
            A_glass (float): Surface area of glass in m².
            temp_func (callable): Function that returns outdoor temperature given time.
        """
        self.t_start = t_start
        self.t_end = t_end
        self.dt = dt
        self.T0 = T0
        self.M = M
        self.c = c
        self.k_fiber = k_fiber
        self.s_fiber = s_fiber
        self.A_fiber = A_fiber
        self.k_glass = k_glass
        self.s_glass = s_glass
        self.A_glass = A_glass
        self.temp_func = temp_func

    def solve(self):
        """Solve the temperature differential equation using Euler's method."""
        n_steps = int((self.t_end - self.t_start) / self.dt)
        t = np.linspace(self.t_start, self.t_end, n_steps)
        T = np.zeros(n_steps)
        T[0] = self.T0

        for i in range(n_steps - 1):
            current_outside_temp = self.temp_func(t[i] % 24)
            dTdt = (1 / (self.M * self.c)) * ((self.k_fiber / self.s_fiber) * self.A_fiber * (current_outside_temp - T[i]) +
                                              (self.k_glass / self.s_glass) * self.A_glass * (current_outside_temp - T[i]))
            T[i + 1] = T[i] + self.dt * dTdt

        return t, T