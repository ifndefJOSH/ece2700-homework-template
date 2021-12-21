#!/usr/bin/python3

if __name__=='__main__':
    courseNum = input("Please input the course number:")
    assnNum = input("Please input the assignment number:")
    problemNumbers = input("Please input the problem numbers (space separated): ").split(' ')
    folder = input("Folder to save to: ")
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
    with open(f"{folder}/hw{assnNum}-Jeppson.tex", "w") as outfile:
        outfile.write(fileContents)
