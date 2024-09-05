def check():
    if not library:
        print("You need to create a list first and the list needs items.")
        removing = False
        break
            
    print("Which list would you like to change?")
    print("Your lists:")
    print(",\n".join("  " + keys for keys in library))
    altering = input().title().strip()
        
    if altering == "" or altering == " ":
        altering = False
        break
