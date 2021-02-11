import os
print("ChickenMcNugget35 Pyinstaller Installer")
INS = input("Action(Install/Uninstall): ") 
PXE = input("Version 3.X or 2.X: ")
print("ChickenMcNugget35 Pyinstaller Installer 1.0")
if  PXE == "2.X" or PXE == "2.x" and INS == "Install":
	print("Sorry :( But this installer is for 3.X only")
	exit()
elif PXE == "3.X" or PXE == "3.x":
	print("Please Wait...")
	print("Executing Installer For v4.2...")
	os.system('pip install pyinstaller')
elif INS == "Uninstall":
        print("Please wait...")
        print("Removing PyInstaller")
        os.system('pip uninstall pyinstaller')
else :
	print("Installer Hex Crash Code 001 :(")
	print("63 6f 6d 6d 61 6e 64 20 6e\n" 
		  "6f 74 20 66 6f 75 6e 64\n")
	print("72 65 73 65 74 20 69 6e 70 75 74\n"
	      " 20 6f 72 20 69 6e 73 74 61 6c 6c\n"
	      " 20 74 79 70 65\n")
  print("Process Has Finished With exit code 1")
