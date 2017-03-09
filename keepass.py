import libkeepass

f = open('liste.txt')
# Wörterbuchliste
fname = '.kdbx'
# KeePass Passwortdatei

for line in f:

line = line.strip()
try:
with libkeepass.open(fname, password=line) as kdb:
print '\n \n Passwort gefunden -- ' + `line`
print '\n Programm wird beendet!'
break
except IOError:
print Falsches Passwort: ' + `line`
