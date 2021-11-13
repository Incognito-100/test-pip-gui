import os
import sys
from time import sleep
from colorama import Fore, Style, init


#==========================================|option 1|==========================================#
def op1():
	command = "pip list"
	relaunch = "pipgui.py"
	
	os.system(command)
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
	
	os.system(command3)
	os.system('cls')
	os.system(relaunch)
#==========================================|option 4|==========================================#
def op4():
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