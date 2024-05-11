#!/usr/bin/python
# -*- coding: utf-8 -*-

#Όρισε τα σύμφωνα
Consonants="BCDFGHJKLMNPQRSTVXZ"
Consonants+=Consonants.lower()
text=raw_input()
newtxt=""
#Για κάθε γράμμα του κειμένου
for i in text:
	#αν το γράμμα είναι σύμφωνο...
	if i in Consonants:
		newtxt+=i+"o"+i.lower()#στην περίπτωση που το σύμφωνο
		#ήταν πρώτο γράμμα και είχε γραφτεί με κεφαλαίο.
	else:
		newtxt+=i
print newtxt
