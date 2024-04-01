#!/usr/bin/env/python3
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
			else:
				break
	def pull(self):
                """Removes and returns the largest item in the queue"""
		result = self.queue[1]
		self.queue[1] = self.queue.pop()
		pointer = 1
		while True:
			if pointer * 2 > self.getLen():
				break
			if self.queue[pointer * 2] >  self.queue[pointer] and (pointer * 2 == len(self.queue) or self.queue[pointer * 2 + 1] < self.queue[pointer]):
				self.queue[pointer], self.queue[pointer * 2] = self.queue[pointer * 2], self.queue[pointer]
			elif self.queue[pointer * 2 + 1] >  self.queue[pointer]:
				self.queue[pointer], self.queue[pointer * 2] = self.queue[pointer * 2], self.queue[pointer]
			else:
				break
		return result
	def getLen(self):
                """Returns the adjusted length of the queue"""
		return len(self.queue) - 1

test = pq()
print("Input: (10, 20, 30, 40, 50)")
for i in (10, 20, 30, 40, 50):
	test.add(i)
print("Sorted:")
print(test.pull())
print(test.pull())
print(test.pull())
print(test.pull())
print(test.pull())