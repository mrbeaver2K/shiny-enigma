class linkedListController():
    def __init__(self):
        self.sentinel = linkedListSentinel(self)
        self.head = self.sentinel
    def append(self, value):
        self.tail.add(value, "i")
    def shift(self):
        self.head = self.head.nextItem
class linkedListNode():
    def __init__(self, value):
        self.value = value
        self.nextItem = None
        self.isSentinel = False
    def add(self, nextItem, mode):
        if self.nextItem != None:
            if mode == "d":
                raise LinkedListRelinkException("NextItem is already defined")
            if mode == "i":
                self.nextItem = linkedListNode(nextItem).add(self.nextItem.value, "d")
            if mode == "a":
                self._parse().add(nextItem, "d")
        else:
            self.nextItem = linkedListNode(nextItem)
        return self
    def _parse(self, distance=-1):
        # Parses until the destination item or the end is reached.
        amount = 0
        item = self
        while True:
            if distance == amount:
                return item
            elif item.nextItem == None or item.nextItem.isSentinel:
                return item
            else:
                item = item.nextItem
                amount += 1
    def parse(self, distance=-1):
        return self._parse(distance).value
    def parseGenerator(self):
        item = self
        while item != None:
            yield item.value
            item = item.nextItem
    def print(self):
        print(self.value, end="")
        if self.nextItem == None or self.nextItem.isSentinel:
            print()
            return
        self.nextItem.print()
class linkedListSentinel(linkedListNode):
    def __init__(self, controller):
        self.controller = controller
        self.isSentinel = True
    def add(self, value):
        if self.controller.head != self:
            raise LinkedListSentinelAddItemException("Sentinel should not be used to define items in a populated list.")
        self.controller.head = linkedListNode(value).add(self,  "d")
        self.controller.tail = self.controller.head
class LinkedListRelinkException(Exception):
    pass
class LinkedListSentinelAddItemException(Exception):
    pass
print("This script adds a linked list implementation")
print("Each linked list extends itself when values are added")
test = linkedListNode(0)
for i in range(0, 10):test.add(i, "a")
print("And they can be emptied back in")
test.print()
