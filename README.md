# botautostart
This is a python file that helps you automatically start all your discord bots with one single script instead of going into each folder and launching each bot manually.
You can also set this script to automatically start at system startup to make it more convenient.

# Works on
Discord.py and/or Discord.js bots

100% tested to work properly on Manjaro (should work on basically all linux distros)

Should work on Windows with WSL (Windows subsystem for Linux) and appropriate dependencies - Untested

Should work on MacOS - Untested (if it doesnt work you might need to switch default shell from zsh to bash)

Works on all processor architectures supported by python

# Setup

Prerequisites-: To use this program, you will need to save all your discord bots into one universal folder (like /home/x/DiscordBots).

Then inside this "root" folder, there should be multiple folders each representing a Discord bot (for example, serverbot, helpbot, etc.)

Then inside that folder you need to have one main.js, index.js, or main.py file, along with anything else you want.

Dependencies -: Python 3.x, Node.js for JS bot (optional), bash.

1. Clone this repo
2. Inside the repo, create a text file called paths.txt, and write all the discord bots (by their name in the folder) that you want to run with the script, seperate by newline.
3. Write the path to your "root" folder, where your discord bots reside, in the bots_folder variable in the python file
4. If you have python 2 installed as well as python3, you might have to set python_start_command variable to python3 if your discord bots run on python3
5. enter your command to startup a command in a certain directory, by editing the shell_cmd variable. However, I recommend keeping it the same and installing gnome-terminal, it is the best!
6. That's it! Now launch this script via `python3 autostartbots.py`, optionally add this to the PATH variable to start from any directory, add this to your application menu so you can easily launch it, and also add the script to system startup.
7. When the script is run, the bots will launch into seperate tabs on the same terminal window. You can now set this terminal window aside on another virtual desktop, and to quit the bots you simply have to close the terminal window. To start them, open the terminal window and run the script. They will all pile up in seperate tabs!
