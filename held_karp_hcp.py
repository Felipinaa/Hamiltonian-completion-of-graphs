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


import itertools


def held_karp(dists):
    """
    Implementation of Held-Karp, an algorithm that solves the Traveling
    Salesman Problem using dynamic programming with memoization.

    Parameters:
        dists: distance matrix

    Returns:
        A tuple, (cost, path).
    """
    n = len(dists)

    # Maps each subset of the nodes to the cost to reach that subset, as well
    # as what node it passed before reaching this subset.
    # Node subsets are represented as set bits.
    C = {}

    # Set transition cost from initial state
    for k in range(1, n):
        C[(1 << k, k)] = (dists[0][k], 0)

    # Iterate subsets of increasing length and store intermediate results
    # in classic dynamic programming manner
    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            # Set bits for all nodes in this subset
            bits = 0
            for bit in subset:
                bits |= 1 << bit

            # Find the lowest cost to get to this subset
            for k in subset:
                prev = bits & ~(1 << k)

                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev, m)][0] + dists[m][k], m))
                C[(bits, k)] = min(res)

    # We're interested in all bits but the least significant (the start state)
    bits = (2**n - 1) - 1

    # Calculate optimal cost
    res = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + dists[k][0], k))
    opt, parent = min(res)

    # Backtrack to find full path
    path = []
    for i in range(n - 1):
        path.append(parent)
        new_bits = bits & ~(1 << parent)
        _, parent = C[(bits, parent)]
        bits = new_bits

    # Add implicit start state
    path.append(0)

    return opt, list(reversed(path))

