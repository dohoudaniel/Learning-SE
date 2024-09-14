# A simple Bubble sort Python file

# 1. An outer loop decreases in size each time
# 2. The goal is to have the largest number at the end of the list when the outer loop completes 1 cycle
# 3. The inner loop starts comparing indexes at the beginning of the loop
# 4. Check if list[index] > list[index + 1]
# 5. If so, swap the index values
# 6. When the inner loop completes the largest number, it is at the end of the list
# 7. Decrement the outer loop by 1

import random
import math

numlist = []
for dan in range(5):
    numlist.append(random.randrange(1, 10))

i = len(numlist) - 1

while i > 1:
    j = 0
    while j < i:
        print("Is {} greater than {}?".format(numlist[j], numlist[j + 1]))
        if numlist[j] > numlist[j + 1]:
            print("Switch", end="\n")
            
            temp = numlist[j]
            numlist[j] = numlist[j + 1]
            numlist[j + 1] = temp
        else:
            print("Don't switch", end="\n")
            # print(clear)
        
        j += 1
        
        for k in numlist:
            print(k, end=", ")
        print()
    
    print("END OF ROUND {}".format(i), end="\n")
    i -= 1

for k in numlist:
    print(k, end=", ")
print()
