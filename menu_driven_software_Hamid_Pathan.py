# IIEC_RISE_Contest
#This code is created by Hamid Pathan (hamidpathan47@gmail.com) from group id IIEC-RISE Python - 89

import os
while True:
	a=input("Chat with me your requirements:")
	if ("don't" in a) or ("never" in a) or ("nope" in a) or ("dont" in a):
		print("please enter valid text and try again")
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a) or ("show" in a)) and (("chrome" in a) or 

("chrome browser" in a) or ("google chrome" in a)):
		os.system('chrome')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a) or ("show" in a)) and (("notepad" in a) or 

("notebook" in a) or ("editor" in a) or ("text" in a)):
		os.system('notepad');
	elif ("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a) and ("firefox" in a):
		os.system('firefox')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("calc" in a) or ("calculator" in a) 

or ("calci" in a)):
		os.system('calc')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("pycharm" in a) or ("py charm" in 

a)):
 		os.system('pycharm')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("msascui" in a) or ("windows 

defender" in a) or ("windows clearner" in a) or ("windows antivirus" in a)):
		os.system('msascui')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("vlc" in a) or ("music player" in 

a)): 
		os.system('vlc')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("picasa" in a) or ("picasa3" in a)):
		os.system('picasa3')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("microphone" in a) or ("micro 

phone" in a)):
		os.system('microphone')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("paint" in a)):
		os.system('paint')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("vmware in")):
		os.system('vmawre')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("AcroRd32" in a) or ("adope rider" 

in a ) or ("adope" in a)):
		os.system('AcroRd32')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and ("camera" in a):
		os.system('camera')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and ("WordPad" in a):
		os.system('WordPad')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and ("Math Input Panel" in a):
		os.system('Math Input Panel')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and ("Sticky Notes" in a):
		os.system('Sticky Notes')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and (("Sound Recorder" in a) or

("recoder" in a)):
		os.system('Sound Recorder')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and ("Windows Media Player" in a):
		os.system('Windows Media Player')
	elif (("run" in a) or ("open" in a) or ("launch" in a) or ("execute" in a)) and ("Windows Media Player" in a):
		os.system('Windows Media Player')
	elif ('exit' in a) or ("stop" in a) or ('quit' in a):
		break
	else:
		print("No apps match your search and try again")
