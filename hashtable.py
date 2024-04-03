class hashtable():
    def __init__(self, m):
        self.m = m
        self.table = [None] * m
    def hash(self, s):
        b = s.encode()
        acc = 1
        for i in b:
            acc = ((acc * 8) + i) % self.m
        return acc
    def add(self, key, value):
        hashedkey = self.hash(key)
        if self.table[hashedkey] != None:
            print(f"Collided! Can\'t store ({key}, {value}) ({hashedkey=})")
            return
        self.table[hashedkey] = (key, value)
with open("tenhundredwordspeopleusethemost.txt", "r") as f:
    h = hashtable(1693)
    for i in f.readlines():
        i = i[:-1]
        h.add(i, i + i)
