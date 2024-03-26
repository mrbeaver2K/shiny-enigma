from time import time
def time_stamp(target):
    start = time()
    target()
    return time() - start
