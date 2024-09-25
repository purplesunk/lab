(* Write a function 
alternate : int list -> int
alternate : int list -> int that takes a list of numbers and adds them with alternating sign. For example 
alternate [1,2,3,4] = 1 - 2 + 3 - 4 = -2
alternate [1,2,3,4] = 1 - 2 + 3 - 4 = -2. *)

fun alternate (lst: int list) =
    let
	fun sum (lst: int list, sign: bool) =
	    if null lst
	    then 0
	    else
		if sign
		then sum(tl lst, not sign) + hd lst
		else sum(tl lst, not sign) - hd lst
    in
	sum(lst, true)
    end

fun min_max (lst: int list) =
    let
	fun get_min(lst: int list, min: int) =
	    if null lst
	    then min
	    else
		if (hd lst) < min
		then get_min(tl lst, hd lst)
		else get_min(tl lst, min)
	fun get_max(lst: int list, max: int) =
	    if null lst
	    then max
	    else
		if (hd lst) > max
		then get_max(tl lst, hd lst)
		else get_max(tl lst, max)
    in
	let val minimum = get_min(tl lst, hd lst)
	in (minimum, get_max(lst, minimum)) end
    end

(* I don't think this is good actually but i don't care *)

fun cumsum (lst: int list) =
    let
	fun sum_last (lst: int list, last: int) =
	    if null lst
	    then []
	    else last + hd lst :: sum_last(tl lst, last + hd lst)
    in
	hd lst :: sum_last(tl lst, hd lst)
    end


fun greeting (s: string option) =
    let
	val name = if isSome s
		   then valOf s
		   else "you"
    in
	"Hello there, " ^ name ^ "!"
    end

	
fun repeat (nums: int list, times: int list) =
    if null nums
    then []
    else if hd times = 0
    then repeat(tl nums, tl times)
    else hd nums :: repeat(nums, hd times - 1 :: tl times)

fun any (lst: bool list) =
    if null (tl lst)
    then hd lst
    else hd lst orelse any(tl lst)

fun all (lst: bool list) =
    if null (tl lst)
    then hd lst
    else hd lst andalso all(tl lst)

fun zip (lst: int list, lst2: int list) =
    if null lst orelse null lst2
    then []
    else (hd lst, hd lst2) :: zip(tl lst, tl lst2)

fun length (lst: int list) =
    if null lst
    then 0
    else 1 + length(tl lst)

fun zipRecycle (lst: int list, lst2: int list) =
    let
	val maxlength =
	    if length lst > length lst2
	    then length lst
	    else length lst2
	fun inZip (l1: int list, l2: int list, len: int) =
	    if len = maxlength
	    then []
	    else (hd l1, hd l2) ::
		 inZip(if null (tl l1) then lst else tl l1,
		       if null (tl l2) then lst2 else tl l2,
		       len + 1)
    in
	inZip(lst, lst2, 0)
    end

(* I don't wanna know how to use the option thingy xdxd *)

fun lookup (pair: (string * int) list, s2: string) =
    if null pair
    then NONE
    else if (#1 (hd pair)) = s2
    then SOME (#2 (hd pair))
    else lookup (tl pair, s2)

fun splitup (lst: int list) =
    if null lst
    then ([], [])
    else
	let val ans = splitup(tl lst)
	in
	    if hd lst = 0
	    then ans
	    else if hd lst > 0
	    then (hd lst :: (#1 ans), #2 ans)
	    else (#1 ans, hd lst :: (#2 ans))
	end

(* I don't know if the treshold should appear on the lists or not *)
fun splitAt (lst: int list, treshold: int) =
    if null lst
    then ([], [])
    else
	let val ans = splitAt(tl lst, treshold)
	in
	    if hd lst = treshold
	    then ans
	    else if hd lst > treshold
	    then (hd lst :: (#1 ans), #2 ans)
	    else (#1 ans, hd lst :: (#2 ans))
	end

fun isSorted (lst: int list) =
    if null (tl lst)
    then true
    else
	hd lst <= hd (tl lst) andalso isSorted(tl lst)

fun isAnySorted (lst: int list) =
    let
	val inc = hd lst <= hd (tl lst)
	fun inIsAnySorted(lst: int list) =
	    if null (tl lst)
	    then true
	    else if inc
	    then hd lst <= hd (tl lst) andalso inIsAnySorted(tl lst)
	    else hd lst >= hd (tl lst) andalso inIsAnySorted(tl lst)
    in
	inIsAnySorted(lst)
    end

fun sortedMerge(l1: int list, l2: int list) =
    if null l1 andalso null l2
    then []
    else if null l1
    then hd l2 :: sortedMerge(l1, tl l2)
    else if null l2
    then hd l1 :: sortedMerge(tl l1, l2)
    else if hd l2 < hd l1
    then hd l2 :: sortedMerge(l1, tl l2)
    else hd l1 :: sortedMerge(tl l1, l2)

fun qsort (lst: int list) =
    if null lst
    then []
    else
	let
	    val pair = splitAt(tl lst, hd lst)
	in
	    qsort(#2 pair) @ hd lst :: qsort(#1 pair)
	end  

fun divide (lst: int list) =
    let
	fun inDivide (lst: int list, pos: bool) =
	    if null lst
	    then ([], [])
	    else
		let
		    val ans = inDivide(tl lst, not pos)
		in
		    if pos
		    then (hd lst :: (#1 ans), #2 ans)
		    else (#1 ans, hd lst :: (#2 ans))
		end
    in
	inDivide(lst, true)
    end

fun not_so_quick_sort (lst: int list) =
    if null lst
    then []
    else if null (tl lst)
    then hd lst :: []
    else
	let
	    val pair = divide(lst)
	in
	    sortedMerge(not_so_quick_sort(#1 pair), not_so_quick_sort(#2 pair))
	end

fun fullDivide (k: int, n: int) =
    let
	fun inFullDivide (d: int, n2: int) =
	    if n2 mod k <> 0
	    then (d, n2)
	    else inFullDivide(d + 1, n2 div k)
    in
	inFullDivide(0, n)
    end

fun factorize (num: int) =
    let
	val sqrt_num = Math.sqrt(Real.fromInt(num))
	fun inFactorize(n: int, left: int) =
	    if left = 1
	    then []
	    else if Real.fromInt(n) > sqrt_num
	    then [(n, 1)]
	    else
		let
		    val pair = fullDivide(n, left)
		    val times = #1 pair
		    val rest = #2 pair
		in
		    if times = 0
		    then inFactorize(n + 1, left)
		    else (n, times) :: inFactorize(n + 1, rest)
		end
    in
	inFactorize(2, num)
    end

fun multiply (lst: (int * int) list) =
    if null lst
    then 1
    else
	let
	    val prime = (#1 (hd lst))
	    val times = (#2 (hd lst))
	in
	    if times = 0
	    then multiply(tl lst)
	    else prime * multiply((prime, times - 1) :: tl lst)
	end

fun pow (n: int, p: int) =
    if p = 0
    then 1
    else n * pow(n, p - 1)

fun multiply_list (lst: int list, n: int) =
    if null lst
    then []
    else hd lst * n :: multiply_list(tl lst, n)

fun products_of_lists (ms: int list, lst: int list) =
    if null ms
    then []
    else multiply_list(lst, hd ms) @ products_of_lists(tl ms, lst)

fun flatten_list (lst: (int list) list) =
    if null lst
    then []
    else hd lst @ flatten_list(tl lst)
	    
fun all_products (lst: (int * int) list) =
    let	
	fun getPowTill(num: int, times: int) =
	    let
		fun inGetList(t: int) =
		    if t > times
		    then []
		    else pow(num, t) :: inGetList(t + 1)
	    in
		inGetList(1)
	    end
		
	fun getLists (lst: (int * int) list) =
	    if null lst
	    then []
	    else getPowTill(#1 (hd lst), #2 (hd lst)) :: getLists(tl lst)

	fun getDivisors (lst: (int list) list) =
	    if null lst
	    then []
	    else products_of_lists(hd lst, flatten_list(tl lst)) @ getDivisors(tl lst)
	val simple_divisors = getLists(lst)
    in
	1 :: flatten_list(simple_divisors) @ getDivisors(simple_divisors)
    end
