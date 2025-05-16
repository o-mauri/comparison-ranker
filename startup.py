## This will take a list of "things" from the input file and convert them into the data file
## to be used in the rest of the program
## this will optionally create a backup of your data file in the backups folder
import shutil

STARTING_SCORE = 1600

def chooseBackup():
    backup = input("Would you like to create a backup? (y/n): ").lower()

    if (not (backup == 'y' or backup == 'n')):
        print("")
        print("Enter a valid option")
        return chooseBackup()
        
    
    return backup == 'y'

def openFile():
    with open("input.txt") as f:
        names = f.readlines()
    
    output = []
    for name in names:
        output.append(name.strip())

    return output

def writeFile(lines):
    with open("data.txt", "w") as f:
        output = []
        for line in lines:
            line = line + ":::" + str(STARTING_SCORE) +'\n'
            output.append(line)
        
        f.writelines(output)

def backupFile():
    save = input("Save Name: ")
    shutil.copyfile("data.txt", "backups/" + save + ".txt")


def runStartup():
    if chooseBackup():
        backupFile()
    writeFile(openFile())

runStartup()