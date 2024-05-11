#!/usr/bin/python
# -*- coding: utf-8 -*-

fin=open("dictionary.txt","r")

words=[]
for line in fin:
	line=line.strip()
	#φτιάξε μία λίστα με όλες τις λέξεις
	words+=line.split()
#Πάρε την κάθε λέξη μία φορά
words=list(set(words))
#Φτιάξε μία λίστα που περιέχει τις λέξεις με το μήκος τους
#Βάζω πρώτο το μήκος για να μη μπερδευτεί το sorting ή κάνω κάτι που
#δεν έχουμε δει στο μάθημα
w=[(len(wrd),wrd) for wrd in words]
w.sort(reverse=True)
print (w)