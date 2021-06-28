import os
import time
import getpass
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

def Pregunta():
	global opc1
	opc1 = int(input("Windows Ownership Reset\n 1) Folder\n 2) File\n\n 0) Exit\n option> "))
	os.system('cls')


def ResetPermisos():
	Pregunta()
	Tk().withdraw()
	os.system('title Windows Ownership Reset ~ By Bluegraded && @echo off && cls')
	#filename = askopenfilename() 
	global filename
	if opc1 == 2:
		filename = askopenfilename(title="Windows Ownership Reset",filetypes=[
		("Select file", "*.*"),("Select folder", "*"),])
	elif opc1 == 1:
		filename = askdirectory(title="Windows Ownership Reset")
		filename = filename
	elif opc1 == 0:
		Menu()
	else:
		Pregunta()
	print(filename)
	comando = '''icacls "'''+filename+'''" /reset /t /c /l'''
	os.system(comando)
	userr = getpass.getuser()
	comando2 = 'mkdir "C:/Users/'+userr+'/Desktop/Copia de Seguridad/"'
	os.system(comando2)
	comando3 = 'copy "'+filename+'/" "C:/Users/'+userr+'/Desktop/Copia de Seguridad/"'
	os.system(comando3)
	#print(comando)
	#print(comando2)
	#print(comando3)
	os.system('cls')
	os.system('color 0f')

def Menu():
	os.system('cls')
	menu = input("MENU\n 1) Simplificar Permisos\n 2) Limpiar Cola Impresora\n\n 0) Exit\n option> ")
	if menu == '0':
		os.system('color 4f && title EXIT && cls')
		print('''	
              _
             | |
             | |===( )   //////
             |_|   |||  | o o|
                    ||| (  _ )                  ____
                     ||| \= /                  ||   \_
                      ||||||                   ||     |
                      ||||||                ...||__/|-"
                      ||||||             __|________|__
                        |||             |______________|
                        |||             || ||      || ||
                        |||             || ||      || ||
------------------------|||-------------||-||------||-||-------
                        |__>            || ||      || ||

                   HIT ANY KEY TO EXIT
		''')
		os.system('pause > null && del null && color 0f')
		exit()
	elif menu == '1':
		ResetPermisos()
	elif menu == '7':
		os.system('net stop spooler && del “%SYSTEMROOT%/System32/spool/printers/*.*” /q /f && net start spooler')
		anan=getpass.getpass('PRESS ANY KEY TO CONTINUE')
	Menu()
Menu()

#rd /s %systemdrive%\$Recycle.Bin /Q
#start taskmgr.exe
#
#        rd C:\Windows\Prefetch\ /Q
#
#        taskkill /F /IM explorer.exe
#
#        ipconfig /release && ipconfig /renew && ipconfig /flushdns

#        Shell("explorer")
#
#        CHKDSK
#        explorer.exe
#
#        DEL /F/Q/S C:\Users\%username%\AppData\Local\Temp\
#
#        && Attrib / d / s - r - h - s * .* && If exist *.lnk del *.lnk && if exist autorun.inf del autorun.inf && pause
#
#        sfc /scannow
#
#        Net stop spooler && del '%SYSTEMROOT%/System32/spool/printers/*.*' /q /f && net start spooler
#
#        rd /s %systemdrive%\$Recycle.Bin /Q
#        """