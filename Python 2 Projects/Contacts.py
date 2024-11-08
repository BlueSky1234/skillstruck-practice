contacts = []
answer = "y"
while answer == "y":
    name = input()
    contacts.append(name)
    answer = input("Would you like to add another?").lower().strip()
    if answer == "y":
        continue
    elif answer == "n":
        
        break
    else:
        print("Invalid Input")
        continue


print(contacts.sort())