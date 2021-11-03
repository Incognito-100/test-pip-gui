import os

menu = input("""
1) list all packages
2) install a package
3) uninstall a package
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