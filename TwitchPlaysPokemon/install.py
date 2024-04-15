import wget
import platform
import os

if os.path.exists("mGBA_Controller_Essentials/mGBASocketServer.lua") == False:
    wget.download("https://github.com/nikouu/mGBA-http/releases/download/0.2.0/mGBASocketServer.lua", out="mGBA_Controller_Essentials/")

elif platform.system() == "Linux":
    if os.path.exists("mGBA_Controller_Essentials/mGBA-http-0.2.0-linux-x64-self-contained") == False:
        wget.download("https://github.com/nikouu/mGBA-http/releases/download/0.2.0/mGBA-http-0.2.0-linux-x64-self-contained", out="mGBA_Controller_Essentials/")
        print("\n\n[DOWNLOAD SUCCESS]: ESSENTIAL FILES FOR LINUX IS INSTALLED!")
        exit()
    else:
        print("[DOWNLOAD ERROR]: ESSENTIAL FILES IS ALREADY INSTALLED")
        exit()

elif platform.system() == "Windows":
    if os.path.exists("mGBA_Controller_Essentials/mGBA-http-0.2.0-win-x64-self-contained.exe") == False:
        wget.download("https://github.com/nikouu/mGBA-http/releases/download/0.2.0/mGBA-http-0.2.0-win-x86-self-contained.exe", out="mGBA_Controller_Essentials/")
        print("\n\n[DOWNLOAD SUCCESS]: ESSENTIAL FILES FOR WINDOWS IS INSTALLED!")
        exit()
    else:
        print("[DOWNLOAD ERROR]: ESSENTIAL FILES IS ALREADY INSTALLED!")
        exit()