
#creates a loop
while True:
    try:

        snicker = input("How many snickers did you get?")
        snicker = int(snicker)

        nerd = input("How many nerds did you get?")
        nerd = int(nerd)
        
        butterfinger = input("How many butterfingers did you get?")
        butterfinger = int(butterfinger)
        total = butterfinger + snicker + nerd


        txt = f"This year, you got {snicker} snickers, {nerd} nerds, and {butterfinger} butterfingers. The total number of these candies is {total} candies."
        print(txt)
        break #Breaks the loop if no errors occur
    
    except ValueError: #Runs if there is an error in previous code and starts the loop over
        print("Invalid Input")
