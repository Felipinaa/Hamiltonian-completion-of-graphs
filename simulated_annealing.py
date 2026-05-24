#Pour la représentation des graphes, on utilise une liste de listes dont les éléments correspondent aux poids des arêtes
#On considère qu'au début, on part d'un dictionnaire tel que les clés correspondent aux sommets, et les éléments associés sont ceux auquels il est relié
#On codera plusieurs fonctions pour se ramener à notre cas d'étude après

##Modules :

import math
import random
import time

##Programmes:

def starting_path(graph):
    return [i for i in range(len(graph))]+[0]

def weight(path, graph):
    w = 0
    n = len(graph)
    for i in range(n-1):
        w+=graph[path[i]][path[i+1]]
    return w + graph[path[n-1]][path[0]]

def replacement_probability(x, y, c):
    return math.exp((x-y)/c)

def simulated_annealing(graph, temperature, cooling_rate, time_limit):
    #Mise en place des variables:
    path = starting_path(graph)
    start=time.time()
    current_path = path
    current_weight = weight(path, graph)
    best_path = current_path
    best_weight = current_weight
    n=len(graph)
    evolution={}
    evolution["choosen variables"]=[temperature, graph, cooling_rate, time_limit]
    evolution["path_evolution"]=[current_path]
    evolution["weight_evolution"]=[current_weight]
    evolution["path_evolution_best"]=[current_path]
    evolution["weight_evolution_best"]=[current_weight]
    evolution["temperature_evolution"]=[temperature]
    evolution["time_evolution"]=[]
    evolution["time_evolution_best"]=[]
    #Programme:
    current_time=0
    while current_time<time_limit:
        new_path = current_path[:] #copie le chemin considéré
        i,j = randint(0,n), randint(0,n) #choisit 2 sommets aléatoirements
        #On créé les solutions proche d'une en permutant 2 sommets aléatoires dans le cycle
        new_path[i], new_path[j] = new_path[j], new_path[i]
        new_weight=weight(new_path, graph)
        if new_weight<current_weight:
            current_path = new_path
            current_weight = new_weight
            evolution["path_evolution"]+=[current_path]
            evolution["weight_evolution"]+=[current_weight]
            evolution["time_evolution"]+= [current_time]
        if new_weight<best_weight:
            best_path = new_path
            best_weight = new_weight
            evolution["path_evolution_best"]+=[current_path]
            evolution["weight_evolution_best"]+=[current_weight]
            evolution["time_evolution_best"]+= [current_time]
        else :
            if random.random()<replacement_probability(current_weight, new_weight, temperature):
                current_path=new_path
                current_weight=new_weight
                evolution["path_evolution"]+=[current_path]
                evolution["weight_evolution"]+=[current_weight]
                evolution["time_evolution"]+= [current_time]
        #Baisse de la température
        temperature *= cooling_rate
        evolution["temperature_evolution"]+=[temperature]
        current_time=time.time()-start
    return evolution
