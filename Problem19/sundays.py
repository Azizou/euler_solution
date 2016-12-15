#!/usr/bin/env python

def is_leap_year(year):
	return year%400==0 or (year%4 == 0 and year%100!=0)

#leap years since start to stop excluding stop
def count_leap_years(start, stop):
	res = 0
	for i in range(start, stop):
		if is_leap_year(i):
			res += 1
	return res

def first_day_of_year(year):
	leaps = count_leap_years(1900, year)
	days = year - 1900 + leaps
	return days%7

def day_to_string(day):
	days = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
	return days[day]

def months_to_days(month,year):
	count = 0
	year = [0,31,28+ int(is_leap_year(year)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	res = 0
	i = 0
	while i < month:
		res += year[i]
		i +=1
	return res

def first_day_of_month(month, year):
	days = months_to_days(month, year) + first_day_of_year(year)
	return days%7


def solve():
	start_m = 1
	start_y = 1901
	stop_m = 12
	stop_y = 2000
	res = 0
	result = []
	for i in range(start_y, stop_y+1):
		for j in range(start_m, stop_m+1):
			if first_day_of_month(j,i) == 6:
				res += 1
				result.append((j,i))
	print result
	return res


def main():
	# print count_leap_years(1900,2000)
	print "Result is: ",solve()
if __name__ == '__main__':
	main()

