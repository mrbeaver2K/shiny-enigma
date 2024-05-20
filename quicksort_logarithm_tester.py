from random import randint
from time import time
import quicksort_logarithm as quicksort
def genArray(size, nSize = 10):
    return [randint(0, nSize) for i in range(0, size)]
print("This script will sort lists of increasing size and display the length, sorting time, and total quicksort recursions, illustrating Quicksort's recursive nature")
n = 10
while n < 100000000:
    testArray = genArray(n)
    amount = sum(testArray)
    start = time()
    quicksort.quicksort(testArray)
    assert sum(testArray) == amount
    for i in range(1, len(testArray) - 1):
        assert testArray[i - 1] <= testArray[i]
    print(n, time() - start, quicksort.maxdepth, sep="\t")
    n *= 10
