import random
minNumber = int(input("input lowest number> "))
maxnumber = int(input("input highest number> "))
with open(input("test file> ")) as file:
    exec(file.read())

while True:
    Target.add(random.randint(minNumber, maxnumber))
