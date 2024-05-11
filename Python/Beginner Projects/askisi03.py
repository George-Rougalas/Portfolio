#!/usr/bin/python
# -*- coding: utf-8 -*-

#Άνοιξε το αρχείο και αποθήκευσε όλο το κείμενο σε μία μεταβλητή
fin=open("keimeno.txt","r")
data=fin.read()
fin.close()
#Εμφάνισε το κείμενο με ανάποδη σειρά
print data[::-1]
#Άνοιξε πάλι το αρχείο
#Οι άλλες επιλογές ήταν ή να κάνω fin.seek(0) πριν κλείσω το αρχείο, αλλά
#δε το είχαμε δει στο μάθημα ή να πάρω το data και να το σπάσω σε γραμμές
fin=open("keimeno.txt","r")
data=fin.readlines()
fin.close()
lines=[]
print "Παλίνδρομα:"

for line in data:
	#Διώξε τα κενά στην αρχή και το τέλος της γραμμής
	line=line.strip()
	#χώρισέ το σε λέξεις
	tmp=line.split()
	for word in tmp:
		#Δες πόσο είναι το μήκος τη λέξης
		if len(word)>2:
			#Δες αν είναι παλίνδρομο
			if word==word[::-1]:
				print word
