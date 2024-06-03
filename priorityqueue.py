#!/usr/bin/env/python3
from random import randint
from time import time
class pq():
	def __init__(self):
		self.queue = [None]
	def add(self, item):
		"""Adds an item to the appropriate place in the queue"""
		self.queue.append(item)
		pointer = self.getLen()
		while pointer > 1:
			if self.queue[pointer] > self.queue[pointer // 2]:
				self.queue[pointer], self.queue[pointer // 2] = self.queue[pointer // 2], self.queue[pointer]
				pointer = pointer // 2
			else:
				break
	def pull(self):
		"""Removes and returns the largest item in the queue"""
		result = self.queue[1]
		if self.getLen() > 1:
			self.queue[1] = self.queue.pop()
			pointer = 1
			while pointer * 2 < self.getLen():
				if self.queue[pointer * 2] >  self.queue[pointer] and self.queue[pointer * 2 + 1] <= self.queue[pointer * 2] or pointer * 2 == len(self.queue):
					self.queue[pointer], self.queue[pointer * 2] = self.queue[pointer * 2], self.queue[pointer]
					pointer = pointer * 2
				elif self.queue[pointer * 2 + 1] >  self.queue[pointer]:
					self.queue[pointer], self.queue[pointer * 2 + 1] = self.queue[pointer * 2 + 1], self.queue[pointer]
					pointer = pointer * 2 + 1
				else:
					break
		else:
			return self.queue.pop()
		return result
	def getLen(self):
		"""Returns the adjusted length of the queue"""
		return len(self.queue) - 1

def run(s, t=1, d=True):
	for i in range(0, t):
		print(s, end="\t" if d else "\n")
		if d:
			print(eval(s))
		else:
			exec(s)

class timeStamp():
	def __init__(self):
		self.reset()
	def reset(self):
		self.start = time()
	def check(self):
		return time() - self.start

test = pq()
print("This code demonstrates a priority queue, first given a set of five random numbers, which it sorts. It then sorts random lists of increasing size (with benchmarks), then retrieves the first element from random lists of increasing size.")
testSet = set()
while len(testSet) < 5:
        testSet.add(randint(0, 50))
#testSet = list(testSet)
print("Input: " + str(testSet))
for i in testSet:
	run(f"test.add({i})", d=False)
print("Sorted:")
run("test.pull()", 5)
print("Sorting an entire list via heaping is O(n log n)")
n = 100
start = timeStamp()
while n <= 10000:
        testArray = [randint(0, n) for i in range(0, n)]
        amount = sum(testArray)
        start.reset()
        test.queue = [None] + testArray
        testArray = []
        for i in range(0, n):
                testArray.append(test.pull())
        assert sum(testArray) == amount
        for i in range(1, len(testArray) - 1):
                assert testArray[i] >= testArray[i]
        print(n, start.check(), sep="\t")
        n *= 10
print("Getting the lowest element from a heap is O(n)")
n = 1000
while n <= 100000:
        testArray = [randint(0, n) for i in range(0, n)]
        start.reset()
        for i in testArray:
                test.add(i)
        test.pull()
        print(n, start.check(), sep="\t")
        n *= 10

