import os
import sys


#Your main bots folder
bots_folder = ""


#Substitute this string with your shell command to
# launch a command in the shell. Where (cmd) is replaced by the command
# and (dir) is replaced by the working directory.
shell_cmd = '''gnome-terminal --tab --working-directory="(dir)" -e "(cmd)" '''

#you might want to change these commands, especially on OSX or linux,
#because python2 is preinstalled. swap between python and python3 to see what works.
python_start_cmd = "python"
node_start_cmd = "node"

def get_cmd(path):
    file = os.path.basename(path)
    dir = os.path.dirname(path)
    if file.endswith(".py"):
        start_cmd = python_start_cmd
    elif file.endswith(".js"):
        start_cmd = node_start_cmd
    cmd = f"{start_cmd} {file}"
    return shell_cmd.replace("(cmd)", cmd).replace("(dir)", dir)


def get_active_file(path):
    keywords = ["main.js", "index.js", "main.py"]
    files = os.listdir(path)
    for keyword in keywords:
        if keyword in files:
            print(f"Found {keyword} in {path}!")
            return os.path.join(path, keyword)
    results = []
    results += [each for each in files if each.endswith('.py') or each.endswith('.js')]
    if len(results) == 1:
        print(f"Found one matching js/py file with unrecognized filename in {path}. Using {results[0]} file.")
        return results[0]
    if len(results) > 1:
        print(f"Found multiple matching js/py files with unrecognized filenames in {path}. Using the first - {results[0]}.") 
        return results[0]
    print(f"Found no matches in {path}! Aborting the mission. Please remove this or comment this from the text file with '#'.")
    return None

def main():
    final_command = ""
    fpaths = open("paths.txt", "r").read().splitlines()
    for path in fpaths:
        if not path.startswith("#"):
            active_file = get_active_file(os.path.join(bots_folder, path))
            if active_file != None:
                final_command += f"{get_cmd(active_file)} &\n"
    final_command += "wait $(jobs -p)"
    print("The final command to be executed: \n", final_command)
    os.system(final_command)

main()
    
