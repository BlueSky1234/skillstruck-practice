#Collects User Input

snicker = input("How many snickers did you get?")
nerd = input("How many nerds did you get?")
butterfinger = input("How many butterfingers did you get?")

#Checks if input is a number 

try:
     
    snicker, nerd, butterfinger = int(snicker), int(nerd), int(butterfinger)

    #Adds the total
    total = snicker + nerd + butterfinger


    txt = f"This year, you got {snicker} snickers, {nerd} nerds, and {butterfinger} butterfingers. The total number of these candies is {total} candies."
    print(txt)

#if there is an error in the try block, the except block will run

except ValueError: 
    print("Invalid Input")

    #Try blocks are used to handle erros, provides program stability, and adds clarity to potential errors.