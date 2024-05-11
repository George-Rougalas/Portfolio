#!/usr/bin/python
# -*- coding: utf-8 -*-

fin=open("arxeio.csv","r")
#Διάβασε όλα τα στοιχεία σε μία λίστα
#Η Python βέβαια έχει και ειδική βιβλιοθήκη για τα αρχεία csv
data=fin.readlines()
fin.close()
names=[]
years=[]
#Για κάθε εγγραφή πάρε τα κατάλληλα πεδια
for rec in data:
	fields=rec.split(",")
	name=fields[0].split()[0]
	names.append(name)
	b=fields[1].split("/")
	years.append(b[2])
#κράτα τις τιμές μόνο μία φορά
unames=list(set(names))
uyears=list(set(years))
max_year=0
cnt_year=0
max_name=""
cnt_name=0
#Βρες το δημοφιλέστερο όνομα
for n in unames:
	tmp=names.count(n)
	if tmp>cnt_name:
		max_name=n
		cnt_name=names.count(n)
#Βρες τη πιο συχνή χρονιά
for y in uyears:
	tmp=years.count(y)
	if tmp>cnt_year:
		max_year=y
		cnt_year=years.count(y)
print max_name,max_year
