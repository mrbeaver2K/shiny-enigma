#!/usr/bin/python3
import random
import time
minNumber = 0
maxnumber = 9

import circularfirstinfirstout
Target = circularfirstinfirstout.circularfirstinfirstout(1000)

start = time.time()
print("Start:", start)

for i in range(0, 10**7):
    Target.add(random.randint(minNumber, maxnumber))

end = time.time()
print("End:", end)
print("Duration:", end - start)
