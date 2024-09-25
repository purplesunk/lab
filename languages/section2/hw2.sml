use "hw2provided.sml";

(* 1 *)
(* a *)
(* string * string list -> string list option *)
fun all_except_option (s, lst) =
    case lst of
	[] => NONE
      | x::xs' => if same_string(s, x)
		  then SOME xs'
		  else case all_except_option(s, xs') of
			   NONE => NONE
			 | SOME l => SOME (x :: l) 


(* b *)
fun get_substitutions1 (subs, s) =
    case subs of
	[] => []
      | x::xs'  => case all_except_option (s, x) of
		       NONE => get_substitutions1(xs', s)
		     | SOME ans => ans @ get_substitutions1(xs', s)

							   
(* c *)
fun get_substitutions2 (subs, s) =
    let
	fun aux (subs, s, acc) =
	    case subs of
		[] => acc
	      | x::xs' => case all_except_option (s, x) of
			      NONE => aux(xs', s, acc)
			    | SOME ans => aux(xs', s, ans @ acc)
    in
	aux(subs, s, [])
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

	
(* 2 *)
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
	[] => false
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
    in
	if sum > goal
	then (sum - goal) * 3
	else if all_same_color cs
	then (goal - sum) div 2
	else goal - sum
    end

	
(* g *)
fun officiate (cs, ms, goal) =
    let
	fun game (cs, ms, hcs) =
	    case ms of
		[] => score (hcs, goal)
	      | Discard(c)::ms' => game (cs, ms', remove_card(hcs, c, IllegalMove))
	      | Draw::ms' => case cs of
				 [] => score (hcs, goal)
			       | c::cs' => if sum_cards (c::hcs) > goal
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

fun check_aces (sum, aces, goal) =
    if sum > goal andalso aces > 0
    then check_aces(sum - 10, aces - 1, goal)
    else sum
	
fun score_challenge (cs, goal) =
    let    
	val sum = check_aces(sum_cards cs, count_aces cs, goal)
    in
	if sum > goal
	then (sum - goal) * 3
	else if all_same_color cs
	then (goal - sum) div 2
	else goal - sum
    end
	
fun officiate_challenge (cs, ms, goal) =
    let
	fun game (cs, ms, hcs) =
	    case ms of
		[] => score_challenge (hcs, goal)
	      | Discard(c)::ms' => game (cs, ms', remove_card(hcs, c, IllegalMove))
	      | Draw::ms' => case cs of
				 [] => score_challenge (hcs, goal)
			       | c::cs' =>
				 let
				     val sum = check_aces(sum_cards (c :: hcs), count_aces (c :: hcs), goal)
				 in
				     if sum > goal
				     then score_challenge ((c :: hcs), goal)
				     else game (cs', ms', (c :: hcs))
				 end
    in
	game(cs, ms, [])
    end


(* b *)
fun search_card(cs, v) =
    case cs of
	[] => NONE
      | c::cs' => if card_value(c) = v
		  then SOME c
		  else search_card(cs', v)

				  
fun careful_player (cs, goal) =
    let
	fun aux (cs, hcs) =
	    let val sum = sum_cards hcs
	    in
		case cs of
		    [] => Draw::[]
		  | c::cs' => if goal - sum > 10
			      then Draw :: aux(cs', c::hcs)
			      else
				  let
				      val diff = sum + card_value(c) - goal
				  in
				      if diff = 0
				      then Draw :: []
				      else
					  case search_card(hcs, diff) of
					      NONE => []
					    | SOME card => Discard(card) :: aux(cs', hcs)
				  end
	    end
    in
	aux (cs, [])
    end
