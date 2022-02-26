import os   # Importing OS module for finding folder location (MIGHT NOT BE NECCESSARY ON A WINDOWS SYSTEM)
import csv  # Importing CSV module for dealing with CSV files


player=str(input("Enter players surname e.g enter 'Kane' for 'Harry Kane': ")) # Asking user for a players surname


with open("03. fpl_weekly.csv",encoding="utf-8") as file: # Opening the csv file and using utf-8 encoding as i get an error otherwise (1)
    reader = csv.reader(file)               # Assigning the data from csv file to reader variable
    for column in reader:                   # Start of linear search algorithm, looping through each line of the file using column variable as the counter
        if player==column[22]:              # comparing input to column[22] which has player surnames.
            print('Name:',column[22],'\n''Total Points',column[29],'\n''Avg Points',column[21],'\n''Goals',column[38],'\n''Assists',column[39],'\n''Clean Sheets',column[40])
            break                           # If the players name is found, information in the identified columns relating to that player will show up, change the number change the data
    else:                                   # break, is the end of the linear search algorithm
        print("Player not found") # If player is not found in the list this is the output


#1. As some players names like Mbappé have characters like é, for some reason i get an issue unless i use the
        # encoding='utf-8' parameter.
#2. Names are case sensitive and if the name has letters such as é, then they need to be put in correctly.
#3. Linear search algorithm used is based on a basic for loop as shown in sample code below.
##myList=[2,19,1,76,54,38,22]
##key=76
##
##for index in range (len(myList)):
##    print("Index value: ",index)
##    if myList[index]==key:
##        print("Key is at location: ",index)
##    else:
##        print("Not found")

#4. Data is pulled from the premier league website but some of the players infor definitely isnt right, such as Wilson has scored a lot of goals but it says 0 in the file itself.
