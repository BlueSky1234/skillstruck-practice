#Imports random generator
import random

#creates a random integer between -10 and 10
x = random.randint(-10,10) 

#if x is greater than 0, then positive will print
if x > 0: 
    print("Positive")

#but if x is the same as zero, then zero will print
elif x == 0: 
    print("Zero")

#if the other statements are false, then negative will print
else: 
    print("Negative")