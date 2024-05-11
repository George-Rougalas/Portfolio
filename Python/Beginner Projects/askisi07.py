#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time

def check_for_prime(p,tests):
	cnt=1
	while cnt<tests:
		a=random.randrange(1,p)
		if pow(a, p,p)==a:
			cnt+=1
		else:
			#αν δε περάσει ένα τεστ δε χρειάζεται να συνεχίζω...
			break
	if cnt==tests:
		return True
	else:
		return False

BITS=int(raw_input("Πόσα bit να είναι ο πρώτος; "))
ts=time.time()
found=False
while not found:
	r=random.randrange(2**(BITS-1),2**BITS)
	found=check_for_prime(r, 10)

print "Πήρε συνολικά %.3f sec για να βρεθεί ο πρώτος: %d" %(time.time()-ts,r)
