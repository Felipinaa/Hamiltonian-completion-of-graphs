import json

with open('infrastructures-reseau-gaz.geojson') as json_file:
    map = json.load(json_file)

def ind(lst, x):
    #Renvoie l'indice d'un élément dans une liste
    for i in range(len(lst)):
        if lst[i]==x:
            return i
    return None

def dict_to_array(graph, order):
    keys=graph.keys()
    n=len(keys)
    tab=[[1 for _ in range(n)] for _ in range(n)]
    for key in keys:
        links = graph[key]
        for vertex in links:
            ind_summit=ind(order, key)
            ind_vertex=ind(order,vertex)
            tab[ind_summit][ind_vertex]=0
    return tab

def create_graph(map):
    graph={} #La représentation en dictionnaire permet de gagner en complexité totale
    order=[] #On a besoin d'un ordre pour pouvoir facilement créer le graphe
    n=len(map["features"])
    for i in range(n):
        region_graph=map["features"][i]["geometry"]["coordinates"]
        m=len(map["features"][i]["geometry"]["coordinates"])
        for j in range(m):
            if map["features"][i]["geometry"]["type"]=="LineString":
                arete=map["features"][i]["geometry"]["coordinates"][j]
                for k in range(2):
                    if arete[k] not in order:
                        #print("single line",arete)
                        graph[arete[k]]=[arete[(k+1)%2]]
                        order.append(arete[k])
                        #Cette vérification est en réalité inutile car la base ne contient pas de doublons
                    elif arete[(k+1)%2] not in graph[arete[k]]:
                        graph[arete[k]].append(arete[(k+1)%2])
            elif map["features"][i]["geometry"]["type"]=="MultiLineString":
                aretes=map["features"][i]["geometry"]["coordinates"][j]
                #print("multi-line",aretes)
                for p in range(len(aretes)):
                    for k in range(2):
                        arete=aretes[p]
                        #print("multi-line object",arete)
                        if arete[k] not in order:
                            graph[arete[k]]=[arete[(k+1)%2]]
                            order.append(arete[k])
                            #Cette vérification est en réalité inutile car la base ne contient pas de doublons
                        elif arete[(k+1)%2] not in graph[arete[k]]:
                            graph[arete[k]].append(arete[(k+1)%2])
    return dict_to_array(graph,order)

graph=create_graph(map)
print(graph)
