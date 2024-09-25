fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* a *)
fun all_except_option (s, lst) =
    case lst of
	[] => NONE
      | x::xs' => if same_string(s, x)
		  then SOME xs'
		  else case all_except_option(s, xs') of
			   NONE => NONE
			 | SOME l => SOME (x :: l) 

(* fun all_except_option (s, lst) = List.filter (fn x => not same_string(s, x)) lst *)

(* b *)
fun get_substitutions1 (subs, s) =
    case subs of
	[] => []
      | x::xs'  => case all_except_option (s, x) of
		       NONE => get_substitutions1(xs', s)
		     | SOME ans => ans @ get_substitutions1(xs', s)

fun get_substitutions1 (subs, s) =
    List.foldl (fn (x, acc) => case all_except_option (s, x) of
				   NONE => acc
				| SOME ans => acc @ ans) [] subs
							   
(* c *)
fun get_substitutions2 (subs, s) =
    let
	fun aux (subs, acc) =
	    case subs of
		[] => acc
	      | x::xs' => case all_except_option (s, x) of
			      NONE => aux(xs', acc)
			    | SOME ans => aux(xs', acc @ ans)
    in
	aux(subs, [])
    end

	
(* d *)
fun similar_names (subs, {first=x, middle=y, last=z}) =
    let
	fun create_names (names) =
	    case names of
		[] => []
	      | n::ns' => {first=n, middle=y, last=z} :: create_names(ns')
    in
	create_names(x :: get_substitutions1(subs, x))
    end

datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* a *)
fun card_color (suit, rank) =
    case suit of
	Spades => Black
      | Clubs => Black
      | Diamonds => Red
      | Hearts => Red


(* b *)
fun card_value (suit, rank) =
    case rank of
	Ace => 11
      | Num(i) => i
      | _ => 10 


(* c *)
fun remove_card (cs, c, e) =		 
    case cs of
	[] => raise e
      | x::xs' => if x = c
		  then xs'
		  else x :: remove_card(xs', c, e)


(* d *)
fun all_same_color (cs) =
    case cs of
	[] => true
      | _::[] => true
      | x::y::xs' => card_color(x) = card_color(y)
		     andalso all_same_color(y::xs')


(* e *)
fun sum_cards (cs) =
    let
	fun aux (cs, acc) =
	    case cs of
		[] => acc
	      | x::xs' => aux(xs', card_value(x) + acc)
    in
	aux (cs, 0)
    end


(* f *)
fun score (cs, goal) =
    let
	val sum = sum_cards cs
	val prelim = if sum > goal
		     then (sum - goal) * 3
		     else goal - sum 
    in
	if all_same_color cs
	then prelim div 2
	else prelim
    end


(* g *)
fun officiate (cs, ms, goal) =
    let
	fun game (cs, ms, hcs) =
	    case (cs, ms) of
		([], []) => score (hcs, goal)
	      | (_, []) => score (hcs, goal)
	      | ([], Draw::_) => score (hcs, goal)
	      | (_, Discard(c)::ms') => game (cs, ms', remove_card(hcs, c, IllegalMove))
	      | (c::cs', Draw::ms') => if sum_cards (c::hcs) > goal
				       then score (c::hcs, goal)
				       else game (cs', ms', c::hcs)
    in
	game(cs, ms, [])
    end


(* 3 *)
(* a *)
fun count_aces (cs) =
    let
	fun aux (cs, acc) =
	    case cs of
		[] => acc
	      | (_, Ace)::cs' => aux(cs', 1 + acc)
	      | _::cs' => aux(cs', acc)
    in aux (cs, 0) end

fun sum_cards_challenge (cs, goal) =
    let
	val aces = count_aces cs
	val sum = sum_cards cs
	fun aux (s, a) =
	    if s > goal andalso a > 0
	    then aux(s - 10, a - 1)
	    else s
    in
	aux (sum, aces)
    end
	
fun score_challenge (cs, goal) =
    let    
	val sum = sum_cards_challenge(cs, goal)
	val prelim = if sum > goal
		     then (sum - goal) * 3
		     else goal - sum 
    in
	if all_same_color cs
	then prelim div 2
	else prelim
    end
	
fun officiate_challenge (cs, ms, goal) =
    let
	fun game (cs, ms, hcs) =
	    case (cs, ms) of
		([], []) => score_challenge (hcs, goal)
	      | ([], Draw::_) => score_challenge (hcs, goal)
	      | (_, []) => score_challenge (hcs, goal)
	      | (_, Discard(c)::ms') => game (cs, ms', remove_card(hcs, c, IllegalMove))
	      | (c::cs', Draw::ms') =>
		    if sum_cards_challenge((c :: hcs), goal) > goal
		    then score_challenge ((c :: hcs), goal)
		    else game (cs', ms', (c :: hcs))
    in
	game(cs, ms, [])
    end


(* b *)
fun search_card (cs, v) =
    case cs of
	[] => NONE
      | c::cs' => if card_value(c) = v
		  then SOME c
		  else search_card(cs', v)

				  
fun careful_player (cs, goal) =
    let
	fun aux (cs, hcs) =
	    let
		val sum = sum_cards hcs
	    in
		if sum = goal
		then []
		else
		    case cs of
			[] => Draw :: []
		      | c::cs' => if goal - sum > 10
				  then Draw :: aux(cs', c::hcs)
				  else let
				      val diff = sum + card_value(c) - goal
				  in
				      if diff = 0
				      then Draw :: []
				      else if diff < 0
				      then Draw :: aux(cs', hcs)
				      else case search_card(hcs, diff) of
					       NONE => []
					     | SOME card => Discard(card) :: Draw :: []
				  end
	    end
    in
	aux (cs, [])
    end
