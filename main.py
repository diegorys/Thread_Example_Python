# -- coding: utf-8 --

"""
 In this example you can learn how to use and communicate two threads in Python.

 Diego de los Reyes Rodríguez.
 v0.0.1 May 2015 - Created.
"""

from random import randint
import threading
import time

'''
Main program. Execute the threads.
'''
def main():
	print "In this example you can learn how to use and communicate two threads in Python."
	print "____________________________________"

	languages = ["Python", "Java", "C#", "PHP", "C++", "Cobol", "Ruby", "C", "ADA", "Lisp", "Prolog"] #List of programming lenguages.
	selected = [0] #Index of the programming language selected.

	threads = list() #List of threads.

	tSelect = threading.Thread(target=select, args=(languages,selected)) #Thread to select programming language.
	tShow = threading.Thread(target=show, args=(languages,selected)) #Thread for showing the selected programming language.

	threads.append(tSelect) #Append the thread to the list.
	threads.append(tShow)

	tSelect.start() #Starts the thread execution.
	tShow.start()

'''
Select a programming language at random.
'''
def select(languages, selected):
	total = len(languages)
	while selected[0] != -1:
		#print "selecting..."
		selected[0] = randint(-1, total-1)
		time.sleep(1)
	for i in range(1,11):
		print "Finishing in",(10-i)
		time.sleep(1)
	print "SELECT: I has finished my execution"

'''
Show the selected programming language.
'''
def show(languages, selected):
	while selected[0] != -1:
		#print "showing..."
		print languages[selected[0]]
		time.sleep(4)
	print "SHOW: I has finished my execution"

main()