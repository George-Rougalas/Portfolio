#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
user_str=raw_input()
#Μπορεί να έχω πολλά περίεργα κενά ανάμεσα στις γραμμές...
user_str=os.linesep.join([s.strip() for s in user_str.splitlines() if s])
#Αφαίρεσε τα πολλαπλά κενά
user_str=" ".join([s.strip() for s in user_str.split(" ") if s])
#Τα σημεία στίξης
points=[".",",",";"]
for p in points:
	user_str=user_str.replace(p,p+" ")
print (user_str)
