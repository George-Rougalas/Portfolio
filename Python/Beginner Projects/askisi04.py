#!/usr/bin/python
# -*- coding: utf-8 -*-

fin=open("test.py","r")
lines=fin.readlines()
fin.close()

#Ο κώδικας δουλεύει για ένα μόνο #...
for line in lines:
	if "#" in line:
		#Αρχίζει από "#";
		l=line.strip()
		if l[0]!="#": #Αν ναι τη αγνοούμε...
			#Χώρισε τη γραμμή σε σχέση με το #
			tmp=line.split("#")
			#Μέτρα πόσα "αυτάκια" υπάρχουν πριν
			a1=tmp[0].count("'")
			a2=tmp[0].count('"')
			#αν είναι μονό το πλήθος
			#πάει να πει ότι το # είναι μέσα σε αλφαριθμητικό
			if a1%2==1 or a2%2==1:
				print line
			else:
				print line.split("#")[0]
	else:
		print line
