(* This are the extra problems in the section 2 *)

datatype 'a tree = leaf 
                 | node of { value : 'a, left : 'a tree, right : 'a tree }
datatype flag = leave_me_alone | prune_me


(* 5 *)
fun tree_height (tree) =
    case tree of
        leaf => 0
      | node {value = _, left = l, right = r} =>
	let val lheight = tree_height(l)
	    val rheight = tree_height(r)
	in 1 + (if lheight > rheight then lheight else rheight)
	end
	    
val tree1 = node { value = 2, left = leaf, right = leaf }
val tree2 = node { value = 3, left = tree1, right = node {value = 7, left = leaf, right = tree1} }
val tree3 = node { value = 4, left = tree2, right = leaf }

val test5 = tree_height(tree3) = 4

(* 6 *)
fun sum_tree (tree) =
    case tree of
	leaf => 0
      | node { value = x, right = r, left = l} =>
	x + sum_tree(r) + sum_tree(l)

val test6 = sum_tree(tree3) = 18

(* 7 *)
fun gardener (tree) =
    case tree of
	leaf => leaf
      | node { value = x, right = r, left = l } =>
	case x of
	    leave_me_alone => node { value = x, right = gardener(r), left = gardener(l) }
	  | prune_me => leaf

val tree4 = node { value = leave_me_alone, right = leaf, left = node { value = prune_me, right = leaf, left = node { value = leave_me_alone, right = leaf, left = leaf }}  }
			    
val test7 = gardener(tree4)


		
