#!/usr/bin/python
# -*- coding: utf-8 -*-

fin=open("test2.py","r")
lines=fin.readlines()
fin.close()
#Οι χαρακτήρες που πρέπει να προσέξω
#Τους έβαλα σε τριπλά ' για να μην έχω πρόβλημα
chrs2check='''[]{}()'"'''
#Χαρακτήρες ανοίγματος
chrOpen="[{("
#Χαρακτήρες κλεισίματος
chrClose="]})"
#Δεν μου αρκεί να δω ότι έχω ίδιο πλήθος "(" με ")" καθώς μπορεί να
#έχω κάτι που τελικά θα είναι της μορφής ({)} που είναι λάθος
cnt=1
foundError=False
for line in lines:
	line=line.strip()
	txt=""
	#Για κάθε γραμμή φτιάχνουμε ένα αλφαριθμητικό
	#που περιέχει τα στοιχεία για έλεγχο με τη σειρά που εμφανίζονται
	for c in line:
		if c in  chrs2check:
			txt+=c
	ops=[]
	#Εδώ μετράμε απλά τα εισαγωγικά
	#Ο τρόπος αυτός πιάνει τα πολλά λάθη, αλλά δεν είναι σωστός
	#π.χ. a="This isn't mine."
	#Το παραπάνω παράδειγμα είναι σωστή δήλωση, αλλά θα φαινόταν λάθος
	#Για να γίνει σωστά πρέπει να γίνει με Regular Expressions
	#εδώ όμως είναι εισαγωγή...
	if txt.count("'")%2==1 or txt.count('"')%2==1:
		print "Λάθος στη γραμμή %d. Πρόβλημα με τα εισαγωγικά." %cnt
		foundError=True
	#Εδώ ελέγχουμε ότι ότι άνοιξε από [({ έκλεισε με τη σωστή σειρά.
	for c in txt:
		if c in chrOpen:
			ops.append(c)
		if c in chrClose:
			if len(ops)==0:
				print "Λάθος στη γραμμή %d. Πρόβλημα με το άνοιγμα/κλείσιμο brackets." % cnt
				foundError=True
			else:
				if c=="]" and ops[-1]=="[":
					ops=ops[:-1]
				elif c=="}" and ops[-1]=="{":
					ops=ops[:-1]
				elif c==")" and ops[-1]=="(":
					ops=ops[:-1]
					print "Λάθος στη γραμμή %d. Πρόβλημα με τη σειρά των brackets." % cnt
				else:
					foundError=True
	cnt+=1
if foundError==True:
	print "Ο κώδικάς σας έχει συντακτικά λάθη."
else:
	print "Ο κώδικάς σας δεν έχει προφανή συντακτικά λάθη."
