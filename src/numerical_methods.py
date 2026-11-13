
import numpy as np

# Differential equation
def cooling_rate(T, Ts, k):
    return -k * (T - Ts)


# Euler method
def euler_method(T0, Ts, k, dt, total_time):

    t = np.arange(0, total_time + dt, dt)
    T = np.zeros(len(t))

    T[0] = T0

    for i in range(len(t) - 1):

        dT = cooling_rate(T[i], Ts, k)

        T[i + 1] = T[i] + dt * dT

    return t, T


# Fourth-order Runge-Kutta method
def rk4_method(T0, Ts, k, dt, total_time):

    t = np.arange(0, total_time + dt, dt)
    T = np.zeros(len(t))

    T[0] = T0

    for i in range(len(t) - 1):

        y = T[i]

        a = cooling_rate(y, Ts, k)
        b = cooling_rate(y + dt*a/2, Ts, k)
        c = cooling_rate(y + dt*b/2, Ts, k)
        d = cooling_rate(y + dt*c, Ts, k)

        T[i + 1] = y + (dt/6)*(a + 2*b + 2*c + d)

    return t, T
