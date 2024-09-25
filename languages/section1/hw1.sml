
fun is_older (date1: int*int*int, date2: int*int*int) =
    if (#1 date1) < (#1 date2)
    then true
    else if (#1 date1) > (#1 date2)
    then false
    else if (#2 date1) < (#2 date2)
    then true
    else if (#2 date1) > (#2 date2)
    then false
    else if (#3 date1) < (#3 date2)
    then true
    else false


fun number_in_month (dates: (int*int*int) list, month: int) =
    if null dates
    then 0
    else if (#2 (hd dates)) = month
    then 1 + number_in_month ((tl dates), month)
    else number_in_month ((tl dates), month)

fun number_in_months (dates: (int*int*int) list, months: int list) =
    if null months
    then 0
    else number_in_month(dates, (hd months)) + number_in_months(dates, tl months)

fun dates_in_month (dates: (int*int*int) list, month: int) =
    if null dates
    then []
    else if (#2 (hd dates)) = month
    then (hd dates) :: dates_in_month((tl dates), month)
    else dates_in_month((tl dates), month)

fun dates_in_months (dates: (int*int*int) list, months: int list) =
    if null months
    then []
    else dates_in_month(dates, hd months) @ dates_in_months(dates, tl months)

							   
fun get_nth (strings: string list, n: int) =
    if n = 1
    then hd strings
    else get_nth(tl strings, n - 1)
							   
							   
(* fun get_nth (strings: string list, n: int) =
    let
	fun count_to_n(s: string list, x: int) =
	    if x = n
	    then hd s
	    else count_to_n(tl s, x + 1)
    in
	count_to_n(strings, 1)
    end *)

		

fun date_to_string (date: int*int*int) =
    let
	val months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    in
	get_nth(months, #2 date) ^ " " ^ Int.toString(#3 date) ^ ", " ^ Int.toString(#1 date)
    end

	
fun number_before_reaching_sum (sum: int, nums: int list) =
    let
	fun sum_list (xs: int list, acc: int, n: int) =
	    if  acc + hd xs >= sum
	    then n - 1
	    else sum_list (tl xs, acc + hd xs, n + 1)
    in
	sum_list(nums, 0, 1)
    end

fun what_month (day: int) =
    let
	val days_of_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    in
	number_before_reaching_sum(day, days_of_months) + 1
    end


fun month_range (day1: int, day2: int) =
    let
	fun get_month (day: int) =
	    if day > day2
	    then []
	    else what_month day :: get_month (day + 1)
    in
	get_month(day1)
    end


fun oldest (dates: (int*int*int) list) =
    if null dates
    then NONE
    else let
	fun oldest_nonempty (dates: (int*int*int) list) =
	    if null (tl dates)
	    then hd dates
	    else let val tl_ans = oldest_nonempty(tl dates)
		 in
		     if is_older(hd dates, tl_ans)
		     then hd dates
		     else tl_ans
		 end
    in
	SOME (oldest_nonempty(dates))
    end


fun remove_duplicates (xs: int list) =
    let
	fun in_list(xs: int list, num: int) =
	    if null xs
	    then false
	    else if num = hd xs
	    then true
	    else in_list(tl xs, num)
			   
	fun add_if_not_in_list(xs: int list, acc: int list) =
	    if null xs
	    then acc
	    else if not (in_list(acc, hd xs))
	    then add_if_not_in_list(tl xs, hd xs :: acc)
	    else add_if_not_in_list(tl xs, acc)
    in
	add_if_not_in_list(xs, [])
    end

fun number_in_months_challenge (dates: (int*int*int) list, months: int list) =
    number_in_months(dates, remove_duplicates(months))

fun dates_in_months_challenge (dates: (int*int*int) list, months: int list) =
    dates_in_months(dates, remove_duplicates(months))

fun get_nth_num (n: int, ns: int list) =
	    if n = 1
	    then hd ns
	    else get_nth_num(n - 1, tl ns)
		   
fun reasonable_date (date: int*int*int) =
    let
	val days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]	
	fun is_leap_year (year: int) =
	    (year mod 4 = 0 andalso year mod 100 <> 0)
	    orelse (year mod 400 = 0 andalso year mod 100 = 0)
	fun get_days (month: int, year: int) =
	    if month = 2 andalso is_leap_year(year)
	    then 29
	    else get_nth_num(month, days)
    in
	(#1 date) > 0 andalso (#2 date) >0 andalso (#3 date) > 0 andalso
	(#2 date) <= 12 andalso (#3 date) <= get_days((#2 date), (#1 date))
    end
