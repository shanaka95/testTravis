from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
g_login = GoogleAuth()
g_login.LoadClientConfigFile("client_secrets.json");
#g_login.LocalWebserverAuth()
g_login.CommandLineAuth()
#g_login.Authorize()
drive = GoogleDrive(g_login)
for i in os.listdir(os.getcwd()+"/downloads"): 
	try:
		print(os.getcwd()+"/downloads/"+i)
		if os.path.isfile(os.getcwd()+"/downloads/"+i):
			print("file")
			upload = drive.CreateFile({'title': i})
			upload.SetContentFile(os.getcwd()+"/downloads/"+i)
			upload.Upload()
			print ('uploade d')
	except Exception as e:
		print (e)