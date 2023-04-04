![image](https://user-images.githubusercontent.com/127352017/229749847-f4aab183-dc2f-47bd-baba-833556b08f59.png)

Bytox is a framework that allows you to use Discord as a command and control centre. It is built mainly on the Discord.py module and also has some C# and C++
incorporated into it's source code. The C2 allows a user to generate a python payload and in the future a C++ payload which will allow them to have control and access to a system. 

**Version 1 has been released. This includes all the python features in the script. C++ aspects are coming very soon**

This is a PoC program, do NOT use this for malicious purposes.

## [Setting up main.py]

firstly, you will need to have a Discord bot set up and get it's token. You can do this at the Discord Developer Portal. Secondly, you will need to run the `Builder.py` script this will install the correct python modules and also build Bytox-C2 for you. All you need to do is follow what it is asking for on screen.

There is a manual way of setting up the script if you would prefer and you can find this in the README.txt file in the repo.

Commands for the C2 can be found by doing [prefix]help in the server. You can also make your .py payload into a Window Executable with pyinstaller and the command:

`pyinstaller [payload.py] --onefile --uac-admin --no-console`

## How to set up the stager

The stager is simple to set up. All you need to do is upload both your payload to a file sharing service and also the `cscapi.dll` than can be created with the `cscapi.cpp` file in visual studio. To do this, create a new C++ Dynamic Link Library solution, copy and past the code and then press build. Now we have all this, you can insert your .exe payload into line 50 of the stager, and your .dll into line 57. 

This will act as a stager to upload your payloads to a target system. It will attempt to start the payload as well as maintain persistence using DLL hooking.
    
