#!/usr/bin/python
# -*- coding: utf-8 -*-
ub=int(raw_input())
#Φτιάξε τη λίστα με όλους τους αριθμούς
primes=range(2,ub+1)
i=0
cur_prime=2
while cur_prime<max(primes):
	j=2
	#Δες από τον επόμενο που έχεις στη λίστα
	for val in primes[i+1:]:
		#Έχει κοινό διαιρέτη;
		if val%primes[i]==0:
			#Αν ναι το αφαιρείς από τη λίστα
			primes.remove(val)
	i+=1
	cur_prime=primes[i]
print primes
