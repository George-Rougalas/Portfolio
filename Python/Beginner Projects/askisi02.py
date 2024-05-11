#!/usr/bin/python
# -*- coding: utf-8 -*-
lb=0
ub=100
while ub-lb>1:
	print "Είσαι μεγαλύτερος από %d;" % ((ub+lb)/2)
	ans=int(raw_input())
	if ans==1:
		lb=(ub+lb)/2
	else:
		ub=(ub+lb)/2
	print lb,ub
print "Είσαι %d;" % (lb)
ans=int(raw_input())
if ans==1:
	print "Το βρήκα!"
else:
	print "Άρα είσαι %d" % (ub)

