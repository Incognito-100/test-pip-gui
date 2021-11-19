import os
import sys
from time import sleep
from colorama import Fore, Style, init


#==========================================|option 1|==========================================#
def op1():
	os.system ("pip list")
	sleep (1)
	os.system("pipgui.py")
	

#==========================================|option 2|==========================================#
def op2():
	instpack = input("> ")


	os.system("pip install " + instpack)
	os.system("cls")    
	os.system("pipgui.py")


#==========================================|option 3|==========================================#
def op3():
	uninstpack = input("> ")
	

	os.system("pip uninstall " + uninstpack)
	os.system("pipgui.py")

#==========================================|option 4|==========================================#

def op4():
	print("type requirements file to install must include directory path")
	
	instrequfile = input("> ")

	os.system("pip install -r " + instrequfile)
	os.system("pipgui.py")


#==========================================|option 5|==========================================#

def op5():
	print("type requirements file to uninstall must include directory path")
	
	uninstrequfile = input("> ")
	
	os.system("pip uninstall -r " + uninstrequfile)
	os.system("pipgui.py")


#==========================================|option 6|==========================================#
def op6():
	print("imput the file path to the python project")
	
	pipreqssetpath = input("> ")
	
	os.system("pipreqs" + pipreqssetpath)
	os.system("pipgui.py")


#==========================================|option 7|==========================================#	
def op7():
	os.system("pip freeze > requirements.txt")

	#==========================================|makes requirements file|==========================================#
	
	reqfile=open('requirements.txt','r')
	file_lines=reqfile.readlines()
	reqfile.close()

	for line in file_lines:
		os.system("pip uninstall -r requirements.txt -y")
		os.system("cls")


	#==========================================|deletes requirements file|==========================================#
	os.system("del requirements.txt")

	#==========================================|clears pip cache|==========================================#
	os.system("pip cache purge")