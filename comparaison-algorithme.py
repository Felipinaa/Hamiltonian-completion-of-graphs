from simulated_annealing import *
from donnees_gaz import *
from ACO import *
from held-karp_hcp import *

import random
import numpy as np
import matplotlib.pyplot as plt

##- Variables globales -##
time_limit = 200 #en s
n=1000
graph_random = [[randint(0,1) for _ in range(n)] for _ in range(n)]
#graph_gaz = donnees_gaz.graph

##-Simulated annealing-##
temperature=300
cooling_rate=0.9
SA_random=simulated_annealing(graph_random, temperature, cooling_rate, time_limit)
#SA_gaz=simulated_annealing(graph_gaz, temperature, cooling_rate, time_limit)

##-Held-karp-##
optimal_weight_random = held-karp(graph_random)
#optimal_weight_gaz = held-karp(graph_gaz)

##-ACO-##
num_ants=50
alpha=0.2
beta=0.3
evaporation_rate=2
Q=100
ants_random = AntColonyOptimization(graph_random, num_ants, time_limit, alpha, beta, evaporatio_rate, Q)
#ants_gaz = AntColonyOptimization(graph_gaz, num_ants, time_limit, alpha, beta, evaporatio_rate, Q)
aco_random = ants_random.optimize() 
#aco_gaz = ants_gaz.optimize()

##-Tracé de l'évolution des poids -##

fig, ax = plt.subplots()
ax.set_title("Tracé de l'évolution du meilleur poids en fonction du temps")
ax.plot(aco_random["time_evolution_best"], aco_random["weight_evolution_best"],label="ACO")
ax.plot(SA_random["time_evolution_best"],SA_random["weight_evolution_best"], label="SA")
ax.plot([0, optimal_weight],[time_limit,optimal_weight], label="optimal weight (HK)")
plt.show()

