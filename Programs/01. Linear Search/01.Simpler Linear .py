myList=['John','Mary','Zoe','Alex','Seamus']
name=str(input("Enter name to lookup:"))

for index in range (len(myList)):
    
    if myList[index]==name:
        print("Key is at location: ",index)
    else:
        print("Not found")
   

