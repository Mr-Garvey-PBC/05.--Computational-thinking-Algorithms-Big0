name=["B","V","D","E","T","F"]

Found=False
Position = 0
Length=len(name)

User_Input=input("Please enter the name you want to search for: ")

while (Found==False) and Position<Length:
    if name[Position]==User_Input:
        Found=True
        print(Position)
    else:
        Position=Position+1

if Found==False:
    print("Item not in Array")
    
