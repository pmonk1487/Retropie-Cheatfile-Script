total=0
more="Yes"
cheats=[]

#Gather information
while more=="Yes":
    cheatName=str(raw_input("What is the name of the cheat?"))

    autoEnable=str(raw_input("Enable the cheat: True/False"))
    autoEnable=autoEnable.lower() #Validate input
    while autoEnable != 'true' and autoEnable !='false':
        print("Enable the cheat: True/False")
        autoEnable=str(raw_input("MUST be \'True\' or \'False\'"))
        autoEnable=autoEnable.lower()

    numLines=input("How many lines are in the cheat?")

    for i in range(numLines): #Input cheats line-by-line
        line=str(raw_input("What is line {0}?".format(i+1)))
        if numLines !=1:
            chtName=cheatName+str(" {0}/{1}".format(i+1,numLines))
        else:
            chtName=cheatName
        cheats.append("cheat{0}_desc = \"{1}\"\ncheat{0}_code = \"{2}\"\ncheat{0}_enable = {3}".format(i+total,chtName,line,autoEnable))
    total+=numLines #Update total lines
    more=raw_input("More? Yes/No").title()
    while more != "Yes" and more != "No": #Validate input
        print("More? Yes/No")
        more=raw_input("MUST be \'Yes\' or \'No\'").title()

#Write to file
filename=str(raw_input("Save To...?"))+".cht"

file = open(filename,'w') 
 
file.write("cheats = {}".format(total))

for x in cheats:
    file.write("\n\n")
    file.write(x)

file.close()
    
