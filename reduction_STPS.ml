(*Le type utilisé pour représenter les graphes sera une liste de listes, et sera transformé en un tableau de tableaux*)

let random_graph n =
  (*créer un graphe aléatoire à n sommets*)
  let graphe = Array.make n [] in
  for i=0 to n-1 do
    let lst = ref [] in
    let k = Random.int n in (*représente le nombre d'arêtes reliés à un sommet*)
    for j=0 to k-1 do
      let s = Random.int n in
      if not (List.mem s !lst) then
        lst := s::!lst
    done;
    graphe.(i)<- !lst
  done;
;;

let conversion_stps graph =
  (*transforme le graphe en un graphe pondéré permettant de se ramener au STPS pour le HCP*)
  let n = Array.length graph in
  (*On a un poids de 0 si l'arête est déjà dans le graphe, sinon 1*)
  let g_stps = Array.make_matrix n n 1 in
  let rec aux graph lst acc =
    match lst with
    |[] -> ()
    |te::qu -> begin
        graph.(acc).(te)<-0;
        aux graph qu acc
          end
  in
  for i=0 to n-1 do
    aux g_stps (graph.(i)) i
  done;
  ;;

(*En réalité, on peut combiner les 2 fonctions en une, créant directement un graphe aléatoire sur lequel on peut appliquer l'algorithme*)

(*Possible de refaire code pour savoir si graphe est hamiltonien ou qhamiltonien à 1 arête près comme vu avec le code python, mais on se focalise directement sur le cas général*)

let rec power2 n =
  match n with
  |0->1
  |_-> let k = power2 (n/2) in
    match n mod 2 with
    |0 -> k*k
    |1 -> 2*k*k
;;

let operation a b func =
  let nb_to_bn n =
    (*convertit le nombre en binaire*)
    let rec aux n acc =
      match n with
      |0-> acc
      |k-> let m = k mod 2 in
        aux (k/2) (m::acc)
    in aux n []
  in
  let bn_to_nb lst =
    let rec aux lst compt =
      match lst with
      |[]-> compt
        (*les bits sont triés dans l'ordre décroissant en terme de poids*)
      |te::qu -> aux qu (compt + te*(power2 (List.length lst))) 
    in aux lst 0
  in
  let rec apply_func b_a b_b acc =
    (*fonction générale faisant une opération sur 2 listes binaires*)
    match b_a, b_b with
    (*matching exhaustif non nécessaire*)
    |[],[]-> acc
    |tea::qua, teb::qub -> apply_func qua qub ((func tea teb)::acc)
  in
  (*convertit le nombre en binaire et applique l'opération*)
  let b_a = ref (nb_to_bn a) in
  let b_b = ref (nb_to_bn b) in
  let l_b = List.length !b_b in
  let l_a = List.length !b_a in
  if l_b > l_a then
    let d = l_b - l_a in
    for i=0 to d-1 do
      b_a := !b_a@[0]
    done; bn_to_nb (apply_func !b_a !b_b [])
  else
    let d = l_a - l_b in
    for i=0 to d-1 do
      b_b := !b_b@[0]
    done; bn_to_nb (apply_func !b_a !b_b [])
;;

let and_b a b =
    let and_bin x y =
      match x, y with
      |1,1 -> 1
      |_,_ -> 0
    in
    operation a b and_bin
;;

let xor_b a b =
  let xor_bin x y =
    match x, y with
    |a, b when a=b -> 0
    |a, b when a<>b -> 1
  in
  operation a b xor_bin
;;

let stpsHBK graph =
  (*création des variables*)
  let n = Array.length graph in
  let pow2_n = power2 n in
  let dp = Array.make_matrix n pow2_n 0 in (*tableau des poids*)
  let path = Array.make_matrix n pow2_n None in (*tableau des chemins*)
  dp.(1).(0) <- 0 (*on prend le sommet 0 comme celui de départ*) ;

  (*parcours des différents sous graphes et chemins*)
  for mask=0 to (pow2_n -1) do
    (*mask correspond à l'identifiant d'un sous-graphe*)
    for i=0 to n-1 do
        (*on parcourt tout les liens d'arêtes possibles*)
      dp.(mask).(i) <- int_of_float(infinity);
      (*regarde si le sous graphe contient i*)
      let pow2_i = power2 i in
      if and_b mask pow2_i <> 0 then
        for j=0 to n-1 do
          let pow2_j = power2 j in
          (*regarde si le sous graphe contient j ou si vérification inutile*)
          if not ( (and_b mask pow2_j = 0) || i=j ) then begin
            let mask_check = (xor_b mask pow2_j) in
            dp.(mask).(j) <- min (dp.(mask).(j)) (dp.(mask_check).(i) + graph.(i).(j)) ;
            path.(mask).(j) <- Some i end
        done;
      done;
   done;

  (*reconstruction du chemin et résultat final*)
  let min_cost = ref (int_of_float infinity) in
  for j=1 to n-1 do
    min_cost:= min (!min_cost) (dp.(pow2_n).(j)+graph.(j).(0))
  done;
  !min_cost
  (*besoin de retourner aussi les chemins représentant ce coût, mais comment ?*)
;;

