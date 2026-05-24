import random
import math
import time

def weight(path, graph):
    #On considère des chemins, donc on veut obtenir un chemin du type i->...->i, d'où la différence avec le SA
    w = 0
    n = len(path)
    for i in range(n-1):
        w+=graph[path[i]][path[i+1]]
    return w

class AntColonyOptimization:
    def __init__(self, graph, num_ants, time_limit, alpha, beta, evaporation_rate, Q):
        self.graph = graph
        self.num_ants = num_ants
        self.time_limit = time_limit
        self.alpha = alpha  # Importance des phéromones
        self.beta = beta    # Priorité en terme de distances
        self.evaporation_rate = evaporation_rate
        self.Q = Q          # Controle intensité des phéromones
        self.pheromones = [[1 for _ in range(len(graph))] for _ in range(len(graph))]  # Matrice des phéromones
        self.best_path = None
        self.best_weight = len(graph) # On peut mettre infini, mais ici correspond à n vu les graphes étudiés
        self.evolution={}
        self.evolution["choosen_variables"]=[num_ants, graph, alpha, beta, evaporation_rate, Q, time_limit]
        starting_path=[i for i in range(len(graph))]+[0]
        starting_weight=weight(starting_path, graph)
        self.evolution["path_evolution_best"]=[starting_path]
        self.evolution["weight_evolution_best"]=[starting_weight]
        self.evolution["pheromones_evolution"]=[self.pheromones]
        self.evolution["time_evolution_best"]=[]
    def calculate_probabilities(self, ant, visited):
        probabilities = []
        current_summit = ant[-1]
        total_pheromone = 0
        for i in range(len(self.graph)):
            if i not in visited:
                pheromone = self.pheromones[current_summit][i] ** self.alpha
                #Necessaire pour ne pas avoir de division par 0
                temporary_weight = weight([current_summit, i], self.graph)
                if temporary_weight!=0:
                    w=temporary_weight ** (-self.beta)
                else:
                    w=0
                total_pheromone += pheromone * w
                probabilities.append(pheromone * w)
            else:
                probabilities.append(0)
        # Normalise les probabibilités
        if total_pheromone > 0:
            probabilities = [p / total_pheromone for p in probabilities]
        return probabilities
    def simulate_ants(self):
        all_ants = []
        for _ in range(self.num_ants):
            ant = [random.randint(0, len(self.graph) - 1)]  # part d'un sommet quelconque
            visited = set(ant)
            while len(visited) < len(self.graph):
                probabilities = self.calculate_probabilities(ant, visited)
                next_summit = random.choices(range(len(self.graph)), weights=probabilities)[0]
                ant.append(next_summit)
                visited.add(next_summit)
            all_ants.append(ant)
        return all_ants
    def update_pheromones(self, all_ants):
        # Evaporate pheromones
        self.pheromones=[[self.pheromones[i][j]*(1-evaporation_rate) for i in range(n)] for j in range(n)]
        self.evolution["pheromones_evolution"]+=[self.pheromones]
        for ant in all_ants:
            path_weight = weight(ant, self.graph)
            pheromone_deposit = self.Q / path_weight
            for i in range(len(ant) - 1):
                self.pheromones[ant[i]][ant[i+1]] += pheromone_deposit
    def optimize(self):
        start=time.time()
        self.evolution["time_evolution_best"]+=[start]
        while time.time()-start<time_limit:
            all_ants = self.simulate_ants()
            self.update_pheromones(all_ants)
            self.evolution["pheromones_evolution"]+=self.pheromones
            for ant in all_ants:
                path_weight = weight(ant, self.graph)
                if path_weight < self.best_weight:
                    self.best_weight = path_weight
                    self.best_path = ant
                    self.evolution["path_evolution_best"]+=[ant]
                    self.evolution["weight_evolution_best"]+=[path_weight]
                    self.evolution["time_evolution_best"]+= [time.time()-start]
        return self.evolution
