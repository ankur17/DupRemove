'''
There can be more than one folder contaning Duplicate 
'''

import os
import sys
p = './Folder'
filePool = list()
all_folder = list()
prime_folder = list()
nprime_folder = list()
del_count = 0
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
for a in prime_folder:
	filePool += os.listdir(os.path.join(p,a))			#!!!Check if the user enters the correct names only like done for all_folder
#folders with duplicate contents
for a in all_folder:
	if a not in prime_folder:
		nprime_folder.append(a)
#removing the content
for fol in nprime_folder:
	for file in os.listdir(os.path.join(p,fol)):
		if file in filePool:
			os.remove(os.path.join(p,fol,file))
			print "Deleted file: "+str(file) + "from folder: " + str(fol)
			del_count += 1
print str(del_count) + " duplicate file(s) deleted"
print "DONE"





