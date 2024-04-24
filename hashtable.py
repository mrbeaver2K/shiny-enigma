from linked_list import *
class hashtable():
    def __init__(self, m):
        self.m = m
        self.table = [None] * m
    def hash(self, s):
        b = s.encode()
        acc = 1
        for i in b:
            acc = ((acc * 8) + i) % self.m
        assert acc <= self.m - 1
        return acc
    def add(self, key, value):
        hashedkey = self.hash(key)
        if self.table[hashedkey] != None:
            #print(f"Collided! Can\'t store ({key}, {value}) ({hashedkey=})")
            return
        if self.table[hashedkey] == None:
            self.table[hashedkey] = linkedListNode((key, value))
        else:
            self.table[hashedkey].add((key,value), "i")
    def lookup(self, key):
        return self.table[self.hash(key)]
    def dekey(self, key):
        self.table[self.hash(key)] = None
    def dump(self):
        return [i for i in self.table if i]
with open("words.txt", "r") as f:
    h = hashtable(10007)
    for i in f.readlines():
        i = i[:-1]
        h.add(i, i + i)
    for i in h.dump():
        print(*list(i.parseGenerator()))
