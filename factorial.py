def factorial(n):
    acc = 1
    for i in range(1, n):
        acc *= i
    return acc

def factorial_recursive(n, p=1):
    if n - 1 > 0:
        return factorial_recursive(n - 1, (n - 1) * p)
    else:
        return p

def run(s):
    print(s, end="\t")
    print(eval(s))

print("We are demonstrating the factorial function two different ways: as a loop and recursively.")
for i in range(0, 16):
    run(f"factorial({i})")
for i in range(0, 16):
    run(f"factorial_recursive({i})")
