import os
import sys


menu = input("""
1) list all packages
2) install a package
3) uninstall a package
4) uninstall all packages
""")

if menu == '1':
	command = "pip list"
	relaunch = "pipgui.py"
	
	os.system(command)
	os.system(relaunch)

if menu == '2':
	instpack = input("> ")
	
	command2 = "pip install " + instpack
	relaunch = "pipgui.py"
	
	os.system(command2)
	os.system(relaunch)

if menu == '3':
	uninstpack = input("> ")
	
	command3 = "pip uninstall " + uninstpack
	relaunch = "pipgui.py"
	
	os.system(command3)
	os.system(relaunch)

if menu == '4':
	command4 = "pip freeze > requirements.txt"

	os.system(command4)
	########### makes requirements file #############################
	
	reqfile=open('requirements.txt','r')
	file_lines=reqfile.readlines()
	reqfile.close()

	for line in file_lines:
		print(line)
		command5 = "pip uninstall -r requirements.txt -y"
		command6 = "cls"
		os.system(command5)
		os.system(command6)

########### deletes requirements file ##############################
	command7 = "del requirements.txt"
	os.system(command7)

############ cleans pip cache ######################################
	command8 = "pip cache purge"
	os.system(command8)