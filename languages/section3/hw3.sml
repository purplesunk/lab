(* Coursera Programming Languages, Homework 3, Provided Code *)

exception NoAnswer

datatype pattern = Wildcard
		 | Variable of string
		 | UnitP
		 | ConstP of int
		 | TupleP of pattern list
		 | ConstructorP of string * pattern

datatype valu = Const of int
	      | Unit
	      | Tuple of valu list
	      | Constructor of string * valu

fun g f1 f2 p =
    let 
	val r = g f1 f2 
    in
	case p of
	    Wildcard          => f1 ()
	  | Variable x        => f2 x
	  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
	  | ConstructorP(_,p) => r p
	  | _                 => 0
    end

(**** you can put all your code here ****)

(* 1 *)
val only_capitals = List.filter (fn x => Char.isUpper(String.sub(x, 0)))

(* 2 *)
val longest_string1 = List.foldl (fn (x, l) => if String.size x > String.size l then x else l) ""

(* 3 *)
val longest_string2 = List.foldl (fn (x, l) => if String.size x >= String.size l then x else l) ""

(* 4 *)
fun longest_string_helper f lst =
    List.foldl (fn (x, l) => if f (String.size x, String.size l) then x else l) "" lst

val longest_string3 = longest_string_helper Int.>

val longest_string4 = longest_string_helper Int.>=

(* 5 *)
val longest_capitalized = longest_string3 o only_capitals
						
(* 6 *)
val rev_string = String.implode o List.rev o String.explode

(* 7 *)
fun first_answer f xs =
    case xs of
	[] => raise NoAnswer
      | x::xs' => case f x of
		      NONE     => first_answer f xs'
		    | SOME ans => ans

(* 8 *)
fun all_answers f xs =
    let fun helper (xs, acc) =
	case xs of
	    []     => SOME acc
	  | x::xs' => case f x of
			  NONE     => NONE
			| SOME ans => helper(xs', acc @ ans)
    in helper(xs, []) end


(* 9a *)
val count_wildcards = g (fn _ => 1) (fn _ => 0)

(* 9b *)
val count_wild_and_variable_lengths = g (fn _ => 1) (fn x => String.size x)

(* 9c *)
fun count_some_var (s, p) =
    g (fn _ => 0) (fn x => if x = s then 1 else 0) p

(* 10 *)
fun check_pat p =
    let fun get_vars (p, acc) =
	    case p of
		Variable x         => x :: acc
	      | TupleP ps          => List.foldl (fn (pa,a) => get_vars (pa,a)) acc ps
	      | ConstructorP(_,pa) => get_vars(pa, acc)
	      | _                  => acc

	fun in_list (x, xs) =
	    case xs of
		[] => false
	      | x'::xs' => x' = x orelse in_list(x, xs')

	fun check_repeat (xs) =
	    case xs of
		[] => false
	      | x::xs' => in_list(x, xs') orelse check_repeat xs'
						     
    in not (check_repeat(get_vars(p, []))) end

(* 11 *)
fun match (v, p) =
    case (v, p) of
	(_, Wildcard)   => SOME []
      | (v, Variable s) => SOME [(s, v)]
      | (Unit, UnitP)   => SOME []
      | (Const x, ConstP y)   => if x = y then SOME [] else NONE
      | (Tuple vs, TupleP ps) => if List.length vs = List.length ps
				 then let val pairs = ListPair.zip (vs, ps)
				      in (all_answers match) pairs end
				 else NONE
      | (Constructor(s1, v), ConstructorP(s2, p)) => if s1 = s2 then match(v, p) else NONE
      | _ => NONE
		 
(* 12 *)
fun first_match v ps =
    SOME (first_answer (fn x => match(v, x)) ps)
    handle NoAnswer => NONE


(**** for the challenge problem only ****)

datatype typ = Anything
	     | UnitT
	     | IntT
	     | TupleT of typ list
	     | Datatype of string
