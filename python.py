import os
import pathlib

os.system('cls')

def GetState():
    stateName = input("Please name a state: ")
    return stateName;

def FormatState(stateVar):
    if len(stateVar) < 8:
        fixedState = stateVar.ljust(8,'*')
        return fixedState
    else:
        return stateVar;

print("1. Get information and display to screen")
print("2. Call user created functions")
print("3. Write list of files to file")
print("4. Read specified file")
print("")
optSel = input("Enter the number of the operation you wish to perform: ")

if optSel == "1":
    companyName = "Dunwoody College"
    programName = "Computer Networking"
    uName = os.environ['UserName']
    classFirst = input("What is the name of your first class? ")
    classSecond = input("What is the name of your second class? ")
    print("You are",uName,"with",programName,"at",companyName)
    print("Your first class is",classFirst,"and your second class is",classSecond)
elif optSel == "2":
    state = GetState()
    newState = FormatState(state)
    print("The formatted version of",state,"is",newState)
elif optSel == "3":
    fileFile = input("What would you like to name the file? ")
    fList = []
    for p in pathlib.Path('.').iterdir():
        if p.is_file():
            fList.append(p)
    with open(fileFile,"w") as myFileWrite:
        myFileWrite.write("These are my files:\n")
        for f in fList:
            myFileWrite.write(f.name)
            myFileWrite.write("\n")
elif optSel == "4":
    readFile = input("Which file would you like to read? ")
    with open(readFile, "r+") as myFileRead:
        print(myFileRead.read())
else:
    print("Canceled. Have a nice day.")