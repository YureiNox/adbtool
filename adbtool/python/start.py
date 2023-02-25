import subprocess
import pyfiglet
import time
import pyperclip
import requests
import shutil
import os
from zipfile import ZipFile 
from time import sleep
import zipfile
import winreg

platform_tools_path = "C:/platform-tools"

print("""          _     _ _                 _     _     _ _              _ _   
__      _| |__ (_) |_ ___ _ __ __ _| |__ | |__ (_) |_       __ _(_) |_ 
\ \ /\ / / '_ \| | __/ _ \ '__/ _` | '_ \| '_ \| | __|____ / _` | | __|
 \ V  V /| | | | | ||  __/ | | (_| | |_) | |_) | | ||_____| (_| | | |_ 
  \_/\_/ |_| |_|_|\__\___|_|  \__,_|_.__/|_.__/|_|\__|     \__, |_|\__|
                                                           |___/       
""")

time.sleep(2)

print('wait for chargement python script...')

time.sleep(1)

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='#'):
	percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
	if iteration == total:
		print()

items = list(range(0, 30))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
for i, item in enumerate(items):
	sleep(0.2)
	loadbar(i + 1, l, prefix='Progress:', suffix='Done', length=l)

time.sleep(2.5)

print('all done !')

os.system('cls' if os.name == 'nt' else 'clear')

time.sleep(2)

def main():
	print("""          _     _ _                 _     _     _ _              _ _   
__      _| |__ (_) |_ ___ _ __ __ _| |__ | |__ (_) |_       __ _(_) |_ 
\ \ /\ / / '_ \| | __/ _ \ '__/ _` | '_ \| '_ \| | __|____ / _` | | __|
 \ V  V /| | | | | ||  __/ | | (_| | |_) | |_) | | ||_____| (_| | | |_ 
  \_/\_/ |_| |_|_|\__\___|_|  \__,_|_.__/|_.__/|_|\__|     \__, |_|\__|
                                                           |___/       
""")
	n = input("1- recovery mod\n2- bootloader mode\n3- other-ascii art\n4- install adb\n5- uninstall all\nPlease enter a number : ")
	
	if n == '1':
		recovery()		
		
		
		
	if n == '2':
		bootloader()
		


	if n == '3':
		other()


	if n == '4':
		adbtool()

	if n == '5':
		uninstall()






def recovery():
	no = input("are you sure you want to reboot in recovery mod? (y/n)")

	if no == 'y':
		subprocess.call([r'C:/adbtool/adb_commande/recovery.bat'])
		os.system('cls' if os.name == 'nt' else 'clear')

	if no == 'n':
		os.system('cls' if os.name == 'nt' else 'clear')
		exit()



def bootloader():
	y = input("are you sure you want to reboot in Bootloader? (y/n)") 
	
	if y == 'y':
		subprocess.call([r'C:/adbtool/adb_commande/bootloader.bat'])
		os.system('cls' if os.name == 'nt' else 'clear')

	if y == 'y':
		os.system('cls' if os.name == 'nt' else 'clear')
		exit()

def uninstall():

    # Remove the platform-tools folder from the Windows PATH environment variable
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS)
    path = winreg.QueryValueEx(key, "Path")[0]
    path = path.replace(platform_tools_path + ";", "")
    winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, path)
    winreg.CloseKey(key)

    # Delete the platform-tools folder
    shutil.rmtree(platform_tools_path)






def other():
	os.system('cls' if os.name == 'nt' else 'clear')
	choice = input("what do you want to do?\n1- assci arts\n2- exit\nenter a number :")

	if choice == '1':
		T = input("Enter Text you want to convert to ASCII art : ")
		ASCII_art_1 = pyfiglet.figlet_format(T)
		print(ASCII_art_1)
		time.sleep(5)
		pyperclip.copy(ASCII_art_1)
		print("your ASCII arts has been copied to the clipboard!")
		time.sleep(3)
		os.system('cls' if os.name == 'nt' else 'clear')

	if choice == '2':
		os.system('cls' if os.name == 'nt' else 'clear')
		exit()
		


def adbtool():
	papath = "C:/platform-tools"

	url = "https://dl.google.com/android/repository/platform-tools-latest-windows.zip?hl=fr"
	file = "platform-tools_r33.0.3-windows.zip"
	
	print('the link to download is:', url)

	sleep(2)

	print('the folder while the software install are:', papath)

	sleep(2)

	ok = input('is it ok y/n:')

	if ok == 'y':


		print('start downloading...')

		sleep(1)

		def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='#'):
			percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration/float(total)))
			filledLength = int(length * iteration // total)
			bar = fill * filledLength + '-' * (length - filledLength)
			print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
			if iteration == total:
				print()

		items = list(range(0, 10))
		l = len(items)

		loadbar(0, l, prefix='Progress:', suffix='Done', length=l)
		for i, item in enumerate(items):
			sleep(0.2)
			loadbar(i + 1, l, prefix='Progress:', suffix='Done', length=l)

		response = requests.get(url)
		with open(file, 'wb') as f:
			f.write(response.content)

		print('download done time to extract..')

		sleep(1.5)

		with zipfile.ZipFile(file, 'r') as zip_ref:
			zip_ref.extractall()

		sleep(1)

		print('extract done')
		sleep(1)
		print('moving file to :', papath)
		shutil.move("platform-tools", "C:/platform-tools")
		sleep(1.5)
		print('cleaning all...')

		sleep(1.5)

		os.remove(file)

		filoo = input('do you want to add adb to path or not yes/no: ')

		

		if filoo == 'yes':
			key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS)
			winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, platform_tools_path + ";%Path%")
			winreg.CloseKey(key)
			print('adding platform-tools to path...')
			sleep(1)
			os.system('cls' if os.name == 'nt' else 'clear')

		if filoo == 'no':
			os.system('cls' if os.name == 'nt' else 'clear')
			main()

		print('all done')

	if ok == 'n':
		exit()
os.system('cls' if os.name == 'nt' else 'clear')
main()
  

	
if __name__ == "__main__":
	main()