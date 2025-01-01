import numpy as np
import matplotlib.pyplot as plt
import argparse



class Parser:

    def __init__(self):
        """ inits Parser with the arguments to take into account"""
        self.parser = argparse.ArgumentParser(description='Standard run of the World3 model.')

        self.parser.add_argument('-birth_rate', default = 0.03, type=float , dest = 'birth_rate',
                                help='Birth rate.')
        
        self.parser.add_argument('-death_rate', default = 0.01, type=float , dest = 'death_rate',
                                help='Death rate.')
        
        self.parser.add_argument('-resource_efficiency', default = 0.02, type=float , dest = 'resource_efficiency',
                                help='Resource efficiency.')
        
        self.parser.add_argument('-pollution_decay', default = 0.005, type=float , dest = 'pollution_decay',
                                help='Pollution decay.')
        
        self.parser.add_argument('-investment_rate', default = 0.2, type=float , dest = 'investment_rate',
                                help='Investment rate.')
        
        self.parser.add_argument('-depreciation_rate', default = 0.1, type=float , dest = 'depreciation_rate',
                                help='Depreciation rate.')
        
        self.parser.add_argument('-industrial_productivity', default = 0.1, type=float , dest = 'industrial_productivity',
                                help='Industrial_productivity.')
        
        self.parser.add_argument('-land_degradation_rate', default = 0.01, type=float , dest = 'land_degradation_rate',
                                help='Land degradation rate.')
        
        self.parser.add_argument('-pollution_impact_on_death', default = 1.0, type=float , dest = 'pollution_impact_on_death',
                                help='Pollution impact on death.')
        
        self.parser.add_argument('-food_impact_on_death', default = 2.0, type=float , dest = 'food_impact_on_death',
                                help='Food impact on death.')
        
        self.parser.add_argument('-initial_population', default = 1.0, type=float , dest = 'initial_population',
                                help='Initial population.')
        
        self.parser.add_argument('-initial_resources', default = 1.0, type=float , dest = 'initial_resources',
                                help='Initial resources.')
        
        self.parser.add_argument('-initial_capital', default = 1.0, type=float , dest = 'initial_capital',
                                help='Initial capital.')
        
        self.parser.add_argument('-initial_food', default = 1.0, type=float , dest = 'initial_food',
                                help='Initial food.')
        
        self.parser.add_argument('-initial_pollution', default = 0.0, type=float , dest = 'initial_pollution',
                                help='Initial pollution.')
        
        self.parser.add_argument('-initial_arable_land', default = 1.0, type=float , dest = 'initial_arable_land',
                                help='Initial food.')
        
        self.parser.add_argument('-name_integrator', default = "RK4", type=str , dest = 'name_integrator',
                                help='Name of numerical integrator for simulating the model.')
        
        self.parser.add_argument('-dt', default = 1.0, type=float , dest = 'dt',
                                help='Timestep for the integrator used to simulate the model.')
        
        self.parser.add_argument('-tmax', default = 200.0, type=float , dest = 'tmax',
                                help='Maximum duration (in year) of the simulation.')
        
        self.args = self.parser.parse_args()
        
        


if __name__ == "__main__":
    
    from model import world3_model
    from integrators import euler_step, rk4_step
    from simulation import simulate_model

    parser = Parser()

    birth_rate = parser.args.birth_rate 
    death_rate = parser.args.death_rate
    resource_efficiency = parser.args.resource_efficiency
    pollution_decay = parser.args.pollution_decay
    investment_rate = parser.args.investment_rate
    depreciation_rate = parser.args.depreciation_rate
    industrial_productivity = parser.args.industrial_productivity
    land_degradation_rate = parser.args.land_degradation_rate
    pollution_impact_on_death = parser.args.pollution_impact_on_death
    food_impact_on_death = parser.args.food_impact_on_death
    params = np.array([birth_rate, 
                       death_rate, 
                       resource_efficiency, 
                       pollution_decay, 
                       investment_rate,
                       depreciation_rate,
                       industrial_productivity,
                       land_degradation_rate,
                       pollution_impact_on_death,
                       food_impact_on_death])
    
    initial_population = parser.args.initial_population
    initial_resources = parser.args.initial_resources
    initial_capital = parser.args.initial_capital
    initial_food = parser.args.initial_food
    initial_pollution = parser.args.initial_pollution
    initial_arable_land = parser.args.initial_arable_land
    state = np.array([initial_population,
                      initial_resources,
                      initial_capital,
                      initial_food,
                      initial_pollution,
                      initial_arable_land])
    
    name_integrator = parser.args.name_integrator
    if name_integrator == "RK4":
        integrator = rk4_step
    else:
        integrator = euler_step
    dt = parser.args.dt
    tmax = parser.args.tmax
    
    # Run simulation
    t, states = simulate_model(world3_model, params, state, integrator, dt, tmax)
    
    # Extract results
    P, R, K_I, F, P_pol, A_land = states.T
    
    # Plot results
    plt.figure(figsize=(12, 8))
    plt.plot(t, P, label="Population (Normalized)")
    plt.plot(t, R, label="Resources")
    plt.plot(t, K_I, label="Industrial Capital")
    plt.plot(t, F, label="Food Production")
    plt.plot(t, P_pol, label="Pollution")
    plt.xlabel("Time (Years)")
    plt.ylabel("Normalized Values")
    plt.title("World3 Model Simulation")
    plt.legend()
    plt.grid()
    plt.show()