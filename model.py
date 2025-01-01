""" This is the World3 model """


import numpy as np


def world3_model(t, state, params):
    P, R, K_I, F, P_pol, A_land = state

    # Extract parameters
    b0 = params[0]
    d0 = params[1]
    resource_efficiency = params[2]
    pollution_decay = params[3]
    investment_rate = params[4]
    depreciation_rate = params[5]
    industrial_productivity = params[6]
    land_degradation_rate = params[7]
    pollution_impact_on_death = params[8]
    food_impact_on_death = params[9]

    # Birth and death rates
    effective_birth_rate = b0 * (F / (1 + F))
    effective_death_rate = (
        d0
        + pollution_impact_on_death * P_pol
        + food_impact_on_death * (1 - F)
    )

    # Population
    dP_dt = P * (effective_birth_rate - effective_death_rate)

    # Resources
    resource_usage_rate = industrial_productivity * K_I / resource_efficiency
    dR_dt = -resource_usage_rate

    # Industrial capital
    industrial_growth = (
        investment_rate
        * industrial_productivity
        * K_I
        * (R / (1 + resource_efficiency * (1 - R)))
    )
    dK_I_dt = industrial_growth - depreciation_rate * K_I

    # Food production
    dF_dt = (F * A_land * industrial_productivity) * (1 - P_pol) - F / P

    # Pollution
    pollution_rate = industrial_productivity * K_I
    dP_pol_dt = pollution_rate - pollution_decay * P_pol

    # Arable land degradation
    dA_land_dt = -land_degradation_rate * P_pol

    # Safeguards to prevent negative values
    dP_dt = max(dP_dt, -P)
    dR_dt = max(dR_dt, -R)
    dK_I_dt = max(dK_I_dt, -K_I)
    dF_dt = max(dF_dt, -F)
    dP_pol_dt = max(dP_pol_dt, -P_pol)
    dA_land_dt = max(dA_land_dt, -A_land)

    return np.array([dP_dt, dR_dt, dK_I_dt, dF_dt, dP_pol_dt, dA_land_dt])