#!/usr/bin/python
# -*- coding: utf-8 -*-

fin=open("keimeno2.txt","r")
unique_words=True
for line in fin:
	line=line.strip()
	words=line.split()
	for w in words:
		letters=[]
		#βάλε τα γράμματα της κάθε λέξης σε μία λίστα
		for l in w:
			letters.append(l)
		#κράτα τα μία φορά
		letters=list(set(letters))
		#Δες αν έχει επαναληφθεί ήδη
		if len(letters)<len(w):
			unique_words=False
			break
		#Θα μπορούσα να κοιτάξω από πριν για να κερδίσω χρόνο
		#if l in letters
	if not unique_words:
		break
print unique_words
