# Mise en place des graphes :

from random import randint

#Non car orienté : on s'intéresse au non-orienté
def random_graphe():
    """Créer un graphe d'étude"""
    n = randint(3, 10)  # Nombre de sommets
    mat = [[randint(0, 1) for _ in range(n)] for _ in range(n)]  # Création de la matrice d'adjacence
    tab = {i: [j for j in range(n) if mat[i][j]] for i in range(n)}
    return mat, tab


def directed_chain_find(graph, k, s):
    """Trouve une chaine de longueur k partant de s"""
    def find_chain(graph, k, s, i, path):
        if i == k:
            return path
        else:
            neighbors = [summit for summit in graph[s] if summit != s]
            for summit in neighbors:
                if summit not in path:
                    path.append(summit)
                    directed_chain_find(graph, k, summit, i+1, path)
    return find_chain(graph, k, s, 0, [])


def separate_graph(graph, div):
    """Sépare graphe en div sous-graphes comportant une chaine parcourant chaque sommet"""
    sub_graphs = []
    research_graph = graph.copy()
    while graph != {}:
        s = 0  # Arbitraire
        path = directed_chain_find(research_graph, div, s)
        for summit in path:
            research_graph.pop(summit)
        sub_graphs.append(path)
    return sub_graphs

def hamiltonian_path_HK(graph):
    n=len(graph) # on peut prendre un n différent pour obtenir tout les chemins de taille n
    dp=[[False for j in range(1<<n)] for i in range(n)] #Vérifie présence chemin hamiltonien
    paths=[[ [] for j in range(1<<n)] for i in range(n)] #Chemin Hamiltonien correspondant
    for i in range(n):
        dp[i][1<<i]= True 
        paths[i][1<<i] = [i] # Chemin pour un singleton : lui-même
    for mask in range(1<<n):
        # mask correspond à un sous graphe parmi les 2**n possibilités
        for vertex in range(n):
            if mask & (1<<vertex)!=0: # Check si le sommet est dans le sous-graph
                mask_check = mask ^ (1<<vertex) #ensemble mask-{vertex} pour le check 
                for k in range(n): #sommet k
                    #check si sommet est dans mask-{vertex} et si on a bien un chemin hamiltonien + une arête reliant le chemin au sommet)
                    if (k!=vertex) and (mask_check & (1<<k)) and (graph[k][vertex] and dp[k][mask_check]): 
                        dp[vertex][mask]= True
                        paths[vertex][mask] = paths[k][mask_check].append(vertex) # Dans code andrei, pred fait référence au prédecesseur.
                        # prend plus de place mais plus accurate pour ce que l'on cherche
                        break 
    for v in range(n):
        #Regarde si il y a un chemin hamiltonien partant de v 
        if dp[v][(1<<n)-1]:
            return (paths, paths[v][(1<<n)-1])
    return (paths, None)

#Quasiment idem que précedemment mais on ne s'intéresse pas au sommet au 0 dans la recherche de chemin hamiltonien
def hamiltonian_cycle_BHK(graph):
    n=len(graph) # on peut prendre un n différent pour obtenir tout les chemins de taille n
    dp=[[False for j in range(1<<n)] for i in range(n)] #Vérifie présence chemin hamiltonien
    paths=[[ [] for j in range(1<<n)] for i in range(n)] #Chemin Hamiltonien correspondant
    for i in range(n):
        dp[i][1<<i]= True 
        paths[i][1<<i] = [i] # Chemin pour un singleton : lui-même
    for mask in range(1<<n):
        # mask correspond à un sous graphe parmi les 2**n possibilités
        if (mask & 1)== 0: # Regarde si on a le sommet 0 dans le cycle
            for vertex in range(1,n):
                if mask & (1<<vertex)!=0: # Check si le sommet est dans le sous-graph
                    mask_check = mask ^ (1<<vertex) #ensemble mask-{vertex} pour le check 
                    for k in range(1,n): #sommet k
                     #check si sommet est dans mask-{vertex} et si on a bien un chemin hamiltonien + une arête reliant le chemin au sommet)
                        if (k!=vertex) and (mask_check & (1<<k)) and (graph[k][vertex] and dp[k][mask_check]): 
                            dp[vertex][mask]= True
                            paths[vertex][mask] = paths[k][mask_check].append(vertex) # Dans code andrei, pred fait référence au prédecesseur.
                         # prend plus de place mais plus accurate pour ce que l'on cherche
                            break 
    # Vérification de la présence d'un cycle : 
    for k in range(1,n):
        if dp[k][(1<<n)-1] and graph[k][0]:
            paths[0][(1<<n)-1] = paths[k][(1<<n)-1].append(0)
            return (paths,paths[0][(1<<n)-1])
    return (paths, None)

def hamiltonian_completion(graph):
    n=len(graph)
    if hamiltonian_cycle_BHK(graph)[1] != None : 
        return "The graph is hamiltonian" 
    elif hamiltonian_path_HK(graph)[1] != None : 
        return "Graph is semi-hamiltonian, link the end and start of the path"
    else:
        paths = hamiltonian_path_HK(graph)[0]
        






    

