class circularfirstinfirstout():
    def __init__(self, targetLength):
        self.buffer = [None] * targetLength
        self.pointer = 0 # Next Available Slot
        self.length = len(self.buffer)
    def add(self, value):
        out = self.buffer[self.pointer]
        self.buffer[self.pointer] = value
        self.pointer = (self.pointer + 1) % self.length
        return out
    def read(self, distance=None):
        modulePointer = self.pointer
        output = []
        while True:
            if distance == None:
                distance = len(self.buffer)
            output.append(self.buffer[modulePointer])
            modulePointer += 1
            if modulePointer == len(self.buffer):
                modulePointer = 0
            distance = distance - 1
            if distance == 0:
                return output
