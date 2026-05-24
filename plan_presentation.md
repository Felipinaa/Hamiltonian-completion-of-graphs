
Première partie : présentation du problème, sa NP-complétude et le but du TIPE (utiliser algos présent pour trouver complexité exponentielle convenable, et potentiellement algorithmes probabibilistes/voir pourquoi ne marchent pas, car sujet assez peu étudié alors que beaucoup de liens avec autres problèmes)
->recherche d'un algorithme diviser pour régner pour résoudre le problème en utilisant chemins eulériens dans des graphes
    =>remise en question du découpage car compliqué à mettre en place + pas de critère pour le faire, détail sur pourquoi ne marchait pas/n'était pas optimal de partir sur ça (lien avec méthode des plusieurs dépots/départs)

Deuxième partie : équivalence du problème avec le TSP en créant un graphe pondéré à partir du graphe étudié, et utilisation de l'algorithme de Held-Karp
-> évoquer algorithme naïf et de backtracking, et pourquoi n'a pas eu besoin d'être implémenté
-> détail de la complexité et du fonctionnement, explique comment permet d'en tirer résultat sur HCP en fonction du poids du chemin retourné, et comment renvoie les différentes arêtes possibles à ajouter au graphe pour le rendre hamiltonien

Troisième partie : recherche d'un algorithme d'approximation permettant d'obtenir une solution approchée
-> découverte de l'algorithme de Christofides, et d'autre permettant d'obtenir solution proche de l'optimal en temps polynomial pour TSP
-> détailler problème de l'espace métrique : besoin que graphe soit métrique (i.e que inégalité triangulaire soit vérifiée pour appliquer algorithmes)
-> pour algo non-métrique, besoin de fixer nombre de triangles ne vérifiant pas inégalité triangulaires/nombres d'arêtes causant que espace pas métrique, et dans un graphe aléatoire dépend de n (analyse probabiliste des différents cas, obtient que dépend de n)
=> rend méthode utilisée impossible à mettre en place dans notre cas, et enlève la complexité polynomiale (la rend factorielle et exponentielle)
    -> possibilité de créer graphes aléatoirement en fixant cette variable, comme dans étude de la HCP en utilisant graphe style G(n,c/n) => utiliser cette construction/raisonnement pour en tirer algorithmes
    -> aussi résultat utilisant espaces "partiellement" métriques (avec le tau) : étudier fonction associant tau (facteur de mesure), a (poids arêtes présentes dans graphe) et b (poids arêtes non présentes dans graphe) renvoyant si espace est partiellement métrique ou pas, car algorithme et permet d'obtenir approximation, et chercher minimum de tau

Quatrième partie : recherche d'une manière de le résoudre de manière pratique et pas théorique/probabiliste
-> méthode du simulated annealing : équivalence avec le TSP permet de trouver cycle hamiltonien facilement de poids <= n (avec méthode 0 et 1). Appliquer méthode (regarder aléatoirement configurations proches) pour réduire coup (se finit que si on trouve une égale à 0, ou après limites de temps)
-> méthode ACO: sorte de machine learning temporaire, va tenter d'explorer différentes possibilités de chemins jusqu'à atteindre un cycle tout en essayant de minimiser poids du chemin (sorte de backtracking mais réfléchi)
-> Possibilité d'utiliser d'autres méthodes (k-opt, trou noir) mais un peu superflu (car déjà 2)

Cinquième partie : comparaison des résultats de manière quantitative, et applications au monde réel
-> transfert de données, étude temporelle des algorithmes et résultat en terme de poids/complétion
-> explication intérêt problème sur connexions hydroliques, électriques ou thermiques : vitesse/distance importe peu (éléments permanents), mais importance d'avoir un cycle et pas de dérivation => d'avoir un cycle hamiltonien. Permet de savoir quels endroits connecter pour faire cela
    => problème de planarité : pas forcément planaires (ex:électricité, eau), même si potentiellement mieux, et si ligne droite est vraiment utile (problème techniques, et importance de la distance aussi quand exagéré)
    => note sur graphes planaires : quasiment impossible dans notre méthode, car création d'un graphe complet (chaque sommet a n degrés, théorème montre que ne peut pas être planaire à un moment ?), donc article un peu inutile

Conclusion :
-> NP-complétude du problème rend difficile à étudier, et sa place dans la catégorie des APX est plus que justifée (i.e difficile d'avoir un algo permettant d'approximer)
-> Ce qu'a apporter : bouger problème dans tout les sens, et recherches sur un problème en utilisant méthodes appliquées à d'autres problèmes : utilisation d'une bibliothèque importante pour une utilisation critique, démarche de recherche




A FAIRE:
Diaporama ++++
Recherche d'une base de données pour appliquer algorithmes ++
Held-Karp : finir/trouver quoi prendre comme données ? 
Faire analyse de performance des différents algorithmes ++
