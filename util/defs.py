import os
import sys
from time import sleep
from colorama import Fore, Style, init


#==========================================|option 1|==========================================#
def op1():
	command = "pip list"
	relaunch = "pipgui.py"
	
	os.system(command)
	sleep(3)
	os.system(relaunch)
	

#==========================================|option 2|==========================================#
def op2():
	instpack = input("> ")
	
	command2 = "pip install " + instpack
	relaunch = "pipgui.py"
	
	os.system(command2)
	os.system('cls')    
	os.system(relaunch)


#==========================================|option 3|==========================================#
def op3():
	uninstpack = input("> ")
	
	command3 = "pip uninstall " + uninstpack
	relaunch = "pipgui.py"
	uninsthelp = "pip list"
	
	os.system(uninsthelp)
	sleep(5)
	os.system(command3)
	os.system('cls')
	os.system(relaunch)


#==========================================|option 4|==========================================#

def op4():
	print("type requirements file to install must include directory path")
	
	instrequfile = input("> ")

	instrequfile2 = "pip install -r " + instrequfile
	relaunch = "pipgui.py"

	os.system(instrequfile2)
	os.system(relaunch)


#==========================================|option 5|==========================================#

def op5():
	print("type requirements file to uninstall must include directory path")
	
	uninstrequfile = input("> ")
	
	uninstrequfile2 = "pip uninstall -r " + uninstrequfile
	relaunch = "pipgui.py"

	os.system(uninstrequfile2)
	os.system(relaunch)


#==========================================|option 6|==========================================#
def op6():
	print("imput the file path to the python project")
	
	pipreqssetpath = input("> ")
	
	commandpipreqs = "pipreqs" + pipreqssetpath
	relaunch = "pipgui.py"

	os.system(commandpipreqs)
	os.system(relaunch)


#==========================================|option 7|==========================================#	
def op7():
	command4 = "pip freeze > requirements.txt"

	os.system(command4)
	#==========================================|makes requirements file|==========================================#
	
	reqfile=open('requirements.txt','r')
	file_lines=reqfile.readlines()
	reqfile.close()

	for line in file_lines:
		command5 = "pip uninstall -r requirements.txt -y"
		command6 = "cls"
		os.system(command5)
		os.system(command6)

	#==========================================|deletes requirements file|==========================================#
	command7 = "del requirements.txt"
	os.system(command7)

	#==========================================|clears pip cache|==========================================#
	command8 = "pip cache purge"
	os.system(command8)