#! /usr/bin/env python

""" Project Euler problem 20"""

def fact(n):
	res = 1
	for i in range(n,0,-1):
		res *= i
	return res	

fact100 =  fact(100)
f100 = str(fact100)
digits_sum = 0
for x in f100:
	digits_sum += int(x)
print digits_sum