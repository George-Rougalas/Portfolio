#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

#Η συνάρτηση αυτή εμφανίζει τη λίστα
#αρχίζοντας το μέτρημα από το 1.
def print_lst(lst):
	res=""
	for i in range(len(lst)):
		res+=" "+str(i+1)+". "+lst[i]
	print res

#Διάβασε όλα τα στοιχεία του αρχείου
fin=open("pokemons.txt","r")
text=fin.read()
fin.close()
#Βάλε όλα τα στοιχεία σε μία λίστα, αφού καθαρίσεις τα διάφορα κενά που μπορεί να έχει το αρχείο
text=os.linesep.join([s.strip() for s in text.splitlines() if s])
text=" ".join([s.strip() for s in text.split(" ") if s])
pokemons=text.split()
print_lst(pokemons)
ans=" "
while ans!="":
	ans=raw_input("Ποιά pokemons θες να αλλάξω; Πάτα <enter> για έξοδο ή τους αριθμούς χωρισμένους με κενά. ")
	ans=ans.strip()
	if " " in ans:
		#Ο χρήστης θα δώσει αριθμούς αυξημένους κατά ένα
		poks=ans.split()
		p1=int(poks[0])-1
		p2=int(poks[1])-1
		#κάνε αντιμετάθεση, στην python μπορούμε και έτσι
		pokemons[p1],pokemons[p2]=pokemons[p2],pokemons[p1]
		print "Η νέα λίστα με pokemon:"
		print_lst(pokemons)
