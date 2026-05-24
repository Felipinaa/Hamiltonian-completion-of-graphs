Plan du TIPE :

-Faire algorithme de Held-Karp pour la complétion hamiltonienne avec le transfert en graphe pondéré : fait
-Mettre en place algorithme de Christofides : pas fait
-> 3 configurations de triangles ne respectent pas inégalité triangulaires sur 8 : à voir impact qu'a sur complexité
-Utilisation des données comme besoin de lier endroits de manière thermique, hydrolique ou électrique (aspect écologique et travaux publics) : pas fait
-Mise en place de l'étude des graphes planaires : pas fait
- k-opt method possible ? (local search)
-simulated annealing idée : bof car besoin de partir de quelque chose, et pas assez de variations entre différents modèles
-ant colony optimisation (peut être mieux car n'utilise pas de métrique) :
-> appliquer algorithme avec comme condition finale un cycle
 => possible de le faire, besoin de tinker avec matrice de phéromones pour affuter résultats

-algo utilisant distances  et triangles : peut être cool si pas beaucoup de triangles ne vérifient pas l'inégalité triangulaire (sinon, en réalité complexité énorme en pratique) -> en réalité, bien plus couteux car quasiment la moitié des triangles ne vérifient pas l'inégalité triangulaire attention : moins de triangles que ça !!!!!!! besoin de trouver nombres triangles, ou est en réalité ça car est complet/total
=> faire un premier check pour enlever un maximum d'arêtes inutiles, permet de réduire drastiquement nombre triangles ne vérifiant pas inégalité, et ainsi d'appliquer algorithme

donc comment le faire ?

-autre méthode pour résolution : mettre poids 1 pour arêtes présentes dans graphe, et nombre très grand devant 1 sinon (pas infini car besoin de les compter), et pas méthode du 0 et du 1 

manière du "nearly metric tsp" : vu que poids arbitraire, possible de trouver un petit tau tq w(a,b)<=tau*(w(a,c)+w(c,b)) pour tout a, b, c sommet, et de pouvoir bound comme cela
=> revient à optimiser tau en fonction de poids arêtes présentes et poids arêtes non présentes => étude de fonction à 2 variables

-> possibilité de combiner nearly metric TSP avec algo paramètre fixé étant nombre d'arêtes à enlever pour rendre métrique : étude de fonctions, mais dépendrait sûrement de n pour complexité 
=> utiliser méthode de création de graphe comme dans article doi math G(n, c/n), et faire varier paramètre c : variations de fonctions difficiles, besoin de faire un plot et d'étudier dérivées en prenant en objet graphe quelconque ?

-> simmulated annealing peut être une bonne solution car on peut très vite trouver un cycle quelconque hamiltonien de poids quelconque (vu que possède toutes les arêtes possibles, revient à par exemple partir de 0 pour aller jusqu'au dernier dans l'ordre, donnant au maximum n en poids), puis de faire ordre dans lequel connecte de manière aléatoire pour minimiser poids






