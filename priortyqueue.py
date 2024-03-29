class pq():
	def __init__(self):
		self.queue = [None]
	def add(self, item):
		self.queue.append(item)
		pointer = self.getLen()
		while pointer > 1:
			if self.queue[pointer] > self.queue[pointer // 2]:
				self.queue[pointer], self.queue[pointer // 2] = self.queue[pointer // 2], self.queue[pointer]
			else:
				break
	def pull(self):
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
		return len(self.queue) - 1
