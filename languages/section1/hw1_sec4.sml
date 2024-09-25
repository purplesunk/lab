(* This is trying with all the things learned *)

fun is_older ((y1, m1, d1), (y2, m2, d2)) =
    y1 < y2 orelse
    y1 = y2 andalso m1 < m2 orelse
    m1 = m2 andalso d1 < d2

fun number_in_month (dates, month) =
    List.foldl (fn ((_, m, _), acc) => if m = month then acc + 1 else acc) 0 dates

fun number_in_months (dates, months) =
    List.foldl (fn (m, acc) => acc + number_in_month(dates, m)) 0 months
			     
fun dates_in_month (dates, month) =
    List.filter (fn (_, m, _) => m = month) dates

fun dates_in_months (dates, months) =
    List.foldl (fn (m, acc) => acc @ dates_in_month(dates, m)) [] months

val get_nth = List.nth

fun date_to_string (year, month, day) =
    let
	val months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    in
	get_nth(months, month) ^ " " ^ Int.toString(day) ^ ", " ^ Int.toString(year)
    end

fun number_before_reaching_sum (sum, lst) =
    let fun nbrs (n, sofar, []) = n
	  | nbrs (n, sofar, x::xs') = 
	    let
		val new = sofar + x
	    in
		if new >= sum
		then n
		else nbrs (n + 1, new, xs')
	    end
    in
	nbrs (0, 0, lst)
    end

fun what_month (days) =
    let val months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    in
	1 + number_before_reaching_sum (days, months_days)
    end

fun month_range (day1, day2) =
    if day1 > day2
    then []
    else what_month(day1) :: month_range(day1 + 1, day2)
