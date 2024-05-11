#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
n=int(raw_input())
lst=[]
for i in range(n):
	lst.append(random.randrange(10))
print lst
#Αργός αλλά απλός τρόπος
#Βάλε σε μία λίστα τα μικρά στοιχεία με τη σειρά τους
low=[x for x in lst if x<5]
#και σε μία τα μεγάλα
high=[x for x in lst if x>=5]
#Ένωσε τις λίστες
print high+low
