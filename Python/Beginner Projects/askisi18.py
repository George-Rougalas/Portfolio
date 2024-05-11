#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
fin=open("keimeno.txt","r")
text=fin.read()
fin.close()
#Μπορεί να έχω πολλά περίεργα κενά ανάμεσα στις γραμμές...
text=os.linesep.join([s.strip() for s in text.splitlines() if s])
#Αφαίρεσε τα πολλαπλά κενά
text=" ".join([s.strip() for s in text.split(" ") if s])
#Χώρισέ το σε λέξεις
words=text.split()
sums=[]
for w in words:
	w=w.upper()
	tmpsum=0
	#βρες το άθροισμα της κάθε λέξης
	for l in w:
		tmpsum+=(ord(l)-64)
	sums.append(tmpsum)
print sums[::-1]
