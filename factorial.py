def factorial(n):
    acc = 1
    for i in range(1, n):
        acc *= i
    return acc

def run(s):
    print(s, end="\t")
    print(eval(s))

print("We are demonstrating the factorial function two different ways: as a loop and recursively.")
for i in range(0, 16):
    run(f"factorial({i})")
