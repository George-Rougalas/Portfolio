#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
LENGTH=raw_input("Πόσα γράμματα να χρησιμοποιήσω; ")
WORDS=raw_input("Πόσες λέξεις να φτιάξω; ")
txt=[]
LETTERS=""
#Φτιάξε μία λίστα με όλα τα γράμματα για να μη τα γράφουμε χειροκίνητα
for i in range(26):
	LETTERS+=chr(i+65)
LETTERS+=LETTERS.lower()
#Πρόσθεσε τυχαία γράμματα
for i in range(LENGTH):
	txt+=LETTERS[random.randrange(len(LETTERS))]
#Πρόσθεσε στο τέλος τα απαραίτητα κενά
txt+=[" "]* (WORDS-1)
#Για να έχω πχ 3 λέξεις πρέπει να έχω δύο κενά
#τα οποία να μην είναι συνεχόμενα και να μην έχουν
#μπει στην αρχή ή στο τέλος
while txt[0]==" " or txt[-1]==" " or "  " in "".join(txt):
	#ανακάτωσε τα στοιχεία
	random.shuffle(txt)
#ενώσέ τα
txt="".join(txt)
#Εγγραφή σε αρχείο
fout=open("rndtext.txt","w")
fout.write(txt)
fout.close()
