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
	os.system(command)

if menu == '2':
	instpack = input("> ")
	
	command = "pip install " + instpack
	
	os.system(command)

if menu == '3':
	uninstpack = input("> ")
	
	command = "pip uninstall " + uninstpack

	os.system(command)

if menu == '4':
	command = "pip freeze > requirements.txt"

	os.system(command)
	########### makes requirements file #############################
	
	reqfile=open('requirements.txt','r')
	file_lines=reqfile.readlines()
	reqfile.close()

	for line in file_lines:
		print(line)
		command2 = "pip uninstall -r requirements.txt -y"
		command3 = "cls"
		os.system(command2)
		os.system(command3)

########### deletes requirements file ##############################
command4 = "del requirements.txt"
os.system(command4)

############ cleans pip cache ######################################
command5 = "pip cache purge"
os.system(command5)