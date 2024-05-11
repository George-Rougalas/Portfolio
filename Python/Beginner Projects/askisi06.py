#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
#Συνάρτηση που μετατρέπει σε διαδικό
#μήκους 8 έναν αριθμό
def binary(x):
	tmp=bin(x)[2:]
	tmp=tmp+"0"*(8-len(tmp))
	return tmp

str1=input()
str2=input()

#Μετέτρεψε κάθε κείμενο σε μία λίστα αριθμών
lst1=[ord(x) for x in str1]
lst2=[ord(x) for x in str2]

binlst1=""
binlst2=""

for i in lst1:
	binlst1+=binary(i)
for i in lst2:
	binlst2+=binary(i)
#Αν έχουν διαφορετικό μήκος πρόσθεσε 8 bit για κάθε χαρακτήρα
cnt=8*(max(len(lst1),len(lst2))-min(len(lst1),len(lst2)))
#Βρες τη διαφορά τους
for i in range(min(len(binlst1),len(binlst2))):
	if binlst1[i]!=binlst2[i]:
		cnt+=1
print (cnt)
