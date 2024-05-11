#!/usr/bin/python
# -*- coding: utf-8 -*-

#Η λίστα με τα σύμφωνα
consonants="bcdfghjklmnpqrstvxz"
#Η λίστα με τα φωνήεντα
vowels="aeiouy"

verb=raw_input("Για ποιό ρήμα θες να βρώ το γερούνδιο; ")
verb=verb.lower()
gerund=""
#Έχει τουλάχιστον 3 γράμματα το ρήμα;
if len(verb)>=3:
	if verb[-3] in consonants and verb[-2] in vowels and verb[-1] in consonants:
		gerund=verb+verb[-1]+"ing"
#Αν δεν βρήκα ήδη το γερούνδιο
#κάνε έλεγχο για τους άλλουν κανόνες
if gerund=="":
	if verb[-2:]=="ie":
		gerund=verb[:-2]+"ying"
	elif verb[-1]=="e":
		gerund=verb[:-1]+"ing"
	else:
		gerund=verb+"ing"
print gerund
