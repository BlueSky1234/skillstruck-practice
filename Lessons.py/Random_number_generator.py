string1 = " We leave in {} minutes "

#Makes the output a random number from 1 - 10
import random
minutes = random.randint(1,10)

print(string1.format(minutes))