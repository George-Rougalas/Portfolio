#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

#Συνάρτηση για να εμφανίζει τη σκακιέρα
def print_board(x):
	for i in range(8):
		print(" ".join(x[i]))

#Συνάρτηση που αλλάζει το περιεχόμενο ανάλλογα με το τι περιέχει
#Αν είχε βασίλισσα και άρα απειλείται, από κεφαλαίο, γίνεται μικρό
#Αν ήταν κενό δείχνει ότι είναι υπό απειλή (δε χρειαζόταν στην άσκηση)
def fix_position(p):
	if p=="Q":
		return "q"
	elif p=="0":
		return "a"
	else:
		return p

#Σταθερά για το πόσες βασίλισσες υπάρχουν στη σκακιέρα
QUEENS=8
#Πρόσθεσε τα αντίστοιχα κομμάτια σε μία λίστα 64 θέσεων
tmp=["0"]*(64-QUEENS)
tmp+=["Q"]*QUEENS
#Ανακάτωσέ τα
random.shuffle(tmp)
board=[]
#Από τις 64 που έχεις, πάρε 8-8 τα στοιχεία και βάλ'τα στη σκακιέρα
for i in range(8):
	board+=[tmp[8*i:8*i+8]]

#Ας δούμε που έχουμε βασίλισσες
for i in range(8):
	for j in range(8):
		#Έλενξε αν στη τρέχουσα θέση έχουμε βασίλισσα που
		#δεν απειλείται, αλλιώς δεν μας νοιάζει
		if board[i][j]=="Q":
			#Φτιάξε τη στήλη
			for k in range(8):
				if k!=i:
					board[k][j]=fix_position(board[k][j])
					#Αν βρέθηκε κάτι,
					#τότε απειλείται και η υπάρχουσα βασίλισσα...
					if board[k][j]=="q":
						board[i][j]="q"
			#Φτιάξε τη γραμμή
			for k in range(8):
				if k!=j:
					board[i][k]=fix_position(board[i][k])
					#Αν βρέθηκε κάτι,
					#τότε απειλείται και η υπάρχουσα βασίλισσα...
					if board[i][k]=="q":
						board[i][j]="q"
			#Φτιάξε τη μία διαγώνιο
			for k in range(8):
			 	if k!=i and k+j-i>=0 and k+j-i<8:
			 		board[k][k+j-i]=fix_position(board[k][k+j-i])
					#Αν βρέθηκε κάτι,
					#τότε απειλείται και η υπάρχουσα βασίλισσα...
					if board[k][k+j-i]=="q":
						board[i][j]="q"
			#Φτιάξε την άλλη διαγωνιο.
			#Άλλος τρόπος, για να εκτιμηθεί ο προηγούμενος...
			ni=i-1
			nj=j+1
			while  0<=nj<8 and 0<=ni<8:
				board[ni][nj]=fix_position(board[ni][nj])
				#Αν βρέθηκε κάτι,
				#τότε απειλείται και η υπάρχουσα βασίλισσα...
				if board[ni][nj]=="q":
					board[i][j]="q"
				ni-=1
				nj+=1
			ni=i+1
			nj=j-1
			while  0<=nj<8 and 0<=ni<8:
				board[ni][nj]=fix_position(board[ni][nj])
				#Αν βρέθηκε κάτι,
				#τότε απειλείται και η υπάρχουσα βασίλισσα...
				if board[ni][nj]=="q":
					board[i][j]="q"
				ni+=1
				nj-=1

#Εμφάνισε τη σκακιέρα
print_board(board)
#Μέτρησε πόσες βασίλισσες δεν απειλούνται
#Μπορούσε να είχε γίνει και πριν αλλά δε
#θα φαινόταν καλά σαν παράδειγμα.
cnt=0
for i in range(8):
	for j in range(8):
		if board[i][j]=="Q":
			cnt+=1
print(cnt)
