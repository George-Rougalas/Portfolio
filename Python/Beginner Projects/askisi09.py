#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
user_str=raw_input()
#Βάλε κάθε χαρακτήρα σε μία λίστα
lst=[]
for i in user_str:
	lst.append(i)
#Ανακάτωσε τη λίστα
random.shuffle(lst)
#Ένωσε όλα τα στοιχεία της λίστας
print "".join(lst)
