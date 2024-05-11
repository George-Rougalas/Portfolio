#!/usr/bin/python
# -*- coding: utf-8 -*-

#Διάβασε το αρχείο
fin=open("prakseis.txt","r")
data=fin.readlines()
fin.close()
#Για κάθε σειρά:
for line in data:
	line=line.strip()
	#Τι πράξη έχουμε;
	if "+" in line:
		op="+"
	elif "-" in line:
		op="-"
	elif "*" in line:
		op="*"
	else:
		op="/"
	#Χώρισε τη γραμμή ανάλογα με τον τελεστή της πράξης
	arg=line.split(op)
	#Αποθήκευσε τον κάθε όρο ξεχωριστά
	arg1=float(arg[0])
	arg2=float(arg[1])
	#Κάνε την αντίστοιχη πράξη
	if op=="+":
		print arg1+arg2
	elif op=="*":
		print arg1*arg2
	elif op=="-":
		print arg1-arg2
	else:
		print arg1/arg2
