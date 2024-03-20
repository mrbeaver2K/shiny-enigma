#!/usr/bin/python3
import random
minNumber = 0
maxnumber = 9

import circularfirstinfirstout
Target = circularfirstinfirstout.circularfirstinfirstout(10)

while True:
    Target.add(random.randint(minNumber, maxnumber))
