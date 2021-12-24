#!/usr/bin/python3

import platform
import os

# Get the filesystem delimiter (/ on linux/mac and \ on windows)
system = platform.system()
if system == "Linux" or system == "Darwin":
    slash = '/'
else:
    slash = '\\'

# Put your last name here as a "constant"
LASTNAME="LASTNAME"

if __name__=='__main__':
    courseNum = input("Please input the course number:")
    assnNum = input("Please input the assignment number:")
    problemNumbers = input("Please input the problem numbers (space separated): ").split(' ')
    print("The folder to save to is an ABSOLUTE path. To get a relative path, prefix the folder with '.'")
    folder = input("Folder to save to: ")
    if folder[0] == '.':
        folder = os.getcwd() + folder[1:]
    pContents = ""
    o = '{'
    c = '}'
    for pNum in problemNumbers:
        pContents += f"""
\\begin{o}problem{c}[{o}{pNum}{c}]
    Given: \\\\
    Find:
\\end{o}problem{c}
\\begin{o}answer{c}
    TODO
\\end{o}answer{c}
        """
    with open('hwtemplate.tex', 'r') as template:
        fileContents = template.read()
    fileContents = fileContents.replace("COURSENUMBER", courseNum)
    fileContents = fileContents.replace("ASSIGNMENTNUMBER", assnNum)
    fileContents = fileContents.replace("CONTENTS", pContents)
    print(f" Saving file to:\n\t{folder}{slash}hw{assnNum}-{LASTNAME}.tex")
    with open(f"{folder}{slash}hw{assnNum}-{LASTNAME}.tex", "w") as outfile:
        outfile.write(fileContents)
