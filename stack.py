class Stack:
    def __init__(self) -> None:
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items) 

s = Stack()
print(s.isEmpty())

s.push(4)
s.push('dog')

print(s.size())
print(s)
print(s.pop())