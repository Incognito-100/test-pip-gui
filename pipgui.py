import os
import sys
from time import sleep
from util.plugins.common import clear, THIS_VERSION, setTitle
from util.defs import op1
from util.defs import op2
from util.defs import op3
from util.defs import op4
from util.defs import op5
from util.defs import op6
from util.defs import op7


#==========================================|auto import/install modules|==========================================#
try: from colorama import Fore, Style, init
except ModuleNotFoundError:
		print(f'\nmodules not found | Installing for you\n')
		os.system("pip install colorama")
		os.system("pip install pipreqs")


#==========================================|menu|==========================================#

def mainmenue():
	setTitle(f"PIP GUI {THIS_VERSION}")
	#Main banner
	clear()
	banner = Style.BRIGHT + f'''{Fore.LIGHTGREEN_EX}
	
                                    ____  ________     ________  ______
                                   / __ \/  _/ __ \   / ____/ / / /  _/
                                  / /_/ // // /_/ /  / / __/ / / // /  
                                 / ____// // ____/  / /_/ / /_/ // /   
                                /_/   /___/_/       \____/\____/___/   
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
					{Fore.RESET}[{Fore.GREEN}1{Fore.RESET}]{Fore.BLACK} list all packages                               
					{Fore.RESET}[{Fore.GREEN}2{Fore.RESET}]{Fore.BLACK} install a package                        
					{Fore.RESET}[{Fore.GREEN}3{Fore.RESET}]{Fore.BLACK} uninstall a package
					{Fore.RESET}[{Fore.GREEN}4{Fore.RESET}]{Fore.BLACK} installs a requirements file
					{Fore.RESET}[{Fore.GREEN}5{Fore.RESET}]{Fore.BLACK} uninstall a requirements file
					{Fore.RESET}[{Fore.GREEN}6{Fore.RESET}]{Fore.BLACK} generate a requirements file
					{Fore.RESET}[{Fore.GREEN}7{Fore.RESET}]{Fore.RED} uninstall all packages 
					{Fore.RESET}[{Fore.GREEN}8{Fore.RESET}]{Fore.RED} exits the program 
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Style.RESET_ALL}'''
	print(banner)
	choice = str(input(
			f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Choice: {Fore.LIGHTRED_EX}'))

	#all options 
	if choice == '1':
		op1()

	elif choice == '2':
		op2()

	elif choice == '3':
		op3()

	elif choice == '4':
		op4()

	elif choice == '5':
		op5()

	elif choice == '6':
		op6()
    
	elif choice == '7':
		op7()

	elif choice == '8':
		clear()
		Style.RESET_ALL
		Fore.RESET
		exit()

	elif choice != '1,2,3,4,5,6,7,8':
        mainmenue()

if __name__ == "__main__":
    sleep(1)
    mainmenue()