class Queue:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item) # O(n)
    
    def dequeue(self):
        return self.items.pop() # O(1)

    def size(self):
        return len(self.items)
