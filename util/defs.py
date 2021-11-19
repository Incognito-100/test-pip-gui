import os
import sys
from time import sleep

#==========================================|auto import/install modules|==========================================#
try: from colorama import Fore, Style, init
except ModuleNotFoundError:
		print(f'\nmodules not found | Installing for you\n')
		os.system("pip install colorama")


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
	print("input the file path to the python project")
	
	pipreqssetpath = input("> ")
	
	os.system("pipreqs" + pipreqssetpath)
	os.system("pipgui.py")


#==========================================|option 7|==========================================#	

def op7():
	os.system("pip freeze > requirements.txt")

#==========================================|makes requirements file|==========================================#	
	
	os.system("pip uninstall -r requirements.txt -y")
	os.system("cls")


#==========================================|deletes requirements file|==========================================#
	
	os.system("del requirements.txt")

#==========================================|clears pip cache|==========================================#
	
	os.system("pip cache purge")