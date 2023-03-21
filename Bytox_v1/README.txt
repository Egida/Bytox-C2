
██████╗ ██╗   ██╗████████╗ ██████╗ ██╗  ██╗
██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔═══██╗╚██╗██╔╝
██████╔╝ ╚████╔╝    ██║   ██║   ██║ ╚███╔╝ 
██╔══██╗  ╚██╔╝     ██║   ██║   ██║ ██╔██╗ 
██████╔╝   ██║      ██║   ╚██████╔╝██╔╝ ██╗
╚═════╝    ╚═╝      ╚═╝    ╚═════╝ ╚═╝  ╚═╝
                                           

- Developed by BlackoutDev -

Bytox is a C2 framework that runs around Discord and it's API. This allows and mitigates any need of knowledge in networking and port forwarding.
Bytox runs on Python, C++ and C# all do and play a vital role in the functionality of Bytox. The stager is created in C# and can be found in the Project1
folder. You will need a coding IDE such as Visual Studio or Visual Studio Code to set up and operate this framework. We would suggest having both. You can
set up the stager simply by following the steps in the "Setting up Bytox Stager" section of this read-me.

The main code for the C2 is in Python and runs on Discord.py so you will need to have this module installed onto your system to be able to run the script.
Bytox also uses D++ too for the C++ varient of the payload you can generate. All links can be found below to the resepctive downloads.

[Setting up main.py]

To set up main.py it is very simple. All you need is a Discord account, a Discord Bot and python installed onto your PC. Once you have these follow tese instructions:

    - Ensure you have Discord.py installed on your system. Run the installer to ensure you have the necessary packages installed on your host machine
    - Copy your bot token and replace line 16 with your token
    - Create a Discord server and a notification channel, also ensure you have Discord Developer Mode on as you will need the channel ID
    - Copy the notification channel ID and then replace line 17 with the new channel ID
    - Inviet your bot the server. Here you can run the main.py script and Bytox should come online and send a message to your notification channels
    - Here you can now type !help and help commands will appear on how to use this framework

[How to use Bytox]

Once you have Bytox setup the commands are simple and easy to follow. You can do the following as of version 1.0.0:
    
    - all_cmd - will attempt to send a command to all the bots connected to the client
    - py_payload - will attempt to generate a python payload
    - set_noti - will change your notification channel
    - more_<command_to_find_more_info - will give you more info about a command


[How to prepare your payloads]

Firstly, PlagaShell is a python script again created on Discord.py that allows you to take control of a target machine with the needs for networking.

To prepare a payload it is very simple all you need to do is follow the command syntax. However, there is some slight preperation you need to do so it works.
You will need another Discord bot which can again be created in the portal and the bot ID. Once your payload has been created you will see that the file is a .py
(python file) and will only run if the target machine has python installed onto the target system. This can be changed with the pyinstaller module in python. Open
your Command Prompt and type the following command:

    pyinstaller [file_name] --onefile --uac-admin --no-console

This will create a Windows Executable file (.exe) that will run on any Windows operating system even without python being installed onto it.

You can also obfuscate the python code before you decide to compile it into a .exe this can be done with Py-Fuscate the link to the github repo can be
found below. 

https://github.com/Sl-Sanda-Ru/Py-Fuscate
