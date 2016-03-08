'''
There can be more than one folder contaning Duplicate 
'''

import os
import sys
p = './Folder'
filePool = list()
all_folder = list()
i = 0 
inls =  sys.argv[1:]
def nameExtract(s):
	l = list()
	tempF = raw_input(s).split("\"")
	for a in range(len(tempF)):
		if a%2:
			l.append(tempF[a])
	return l
#if inls[0]=="--help":
#	print "I will help you buddy"
all_folder = nameExtract("Enter the Folder name(s) containing duplicate files: ")
while True:
	a = all_folder[i]
	if a not in os.listdir(p):
		print str(a) +"is misspelled",
		all_folder.remove(a)
		all_folder.append(raw_input("Re-Enter the name: ").strip("\""))
	else:
		i+=1
	if i>=len(all_folder):
		break

prime_folder = nameExtract("Folder name(s) of original content: ")
print prime_folder
for a in prime_folder:
	filePool += os.listdir(os.path.join(p,a))			#Check if the user enters the correct names only
print filePool



#print sys.argv[1]

