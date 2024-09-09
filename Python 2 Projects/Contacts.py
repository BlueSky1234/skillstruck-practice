contacts = []
updating = True
while updating:
    try:
        print("New contact's name")
        name = input().strip()
        if name and not any(x in name for x in "\n\t\r"):
            contacts.append(name)
            answer = input("Would you like to add another?").lower().strip()
            if answer == "y":
                continue
            elif not answer or answer == "n":
                updating = False
                break
            else:
                print("Invalid Input")
                continue
        else:
            if contacts:
                print("Contacts saved")
                print("\n".join(name for name in sorted(contacts)))
                updating = False
                break
    except KeyboardInterrupt: 
        break