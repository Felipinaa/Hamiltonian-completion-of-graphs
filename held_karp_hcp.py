#On considère un graphe déjà mis sous le bon format

from math import *

def held-karp(graph):
    #Création des variables
    n=len(graph)
    pow2_n = 2**n
    dp = [[0 for _ in range(n)] for _ in range(pow2_n)] #Tableau des poids
    path = [[None for _ in range(n)] for _ in range(pow2_n)] #Tableau des chemins
    dp[1][0] = 0
    #Parcours des différents sous-graphes et chemins
    for mask in range(pow2_n):
        for i in range(n):
            #On parcout tout les liens d'arêtes possibles
            dp[mask][i]=inf
            pow2_i=2**i
            if mask & pow2_i != 0:
                for j in range(n):
                    pow2_j = 2**j
                    if not((mask & pow2_j == 0) or i=j):
                        mask_check = mask ^ pow2_j
                        dp[mask][j]=min(dp[mask][j], dp[mask_check][i]+graph[i][j])
                        path[mask][j]=i
    min_cost = inf
    for j in range(1,n):
        min_cost=min(min_cost, dp[pow2_n][j]+graph[j][0])
    return min_cost
