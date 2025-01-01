""" Numerical integrators for solving the model equations """


import numpy as np


# Euler Integrator
def euler_step(func, t, state, dt, params):
    return np.maximum(state + dt * func(t, state, params), 0)

# RK4 Integrator
def rk4_step(func, t, state, dt, params):
    k1 = func(t, state, params)
    k2 = func(t + dt / 2, state + dt / 2 * k1, params)
    k3 = func(t + dt / 2, state + dt / 2 * k2, params)
    k4 = func(t + dt, state + dt * k3, params)
    next_state = state + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return np.maximum(next_state, 0)  # Ensure no negative values in state