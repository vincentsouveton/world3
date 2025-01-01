""" Simulation function for evolving the model through time """


import numpy as np


# Simulation
def simulate_model(model, params, state, integrator, dt, t_max):
    t = np.arange(0, t_max, dt)
    states = [state]
    for time in t[:-1]:
        state = integrator(model, time, state, dt, params)
        states.append(state)
    return t, np.array(states)