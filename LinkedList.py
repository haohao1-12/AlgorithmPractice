# 采用链表实现无序表
# 为了实现无序表的数据结构， 可以采用链接表的方案
# 虽然列表数据结构要求保持数据项前后的相对位置，但这种前后位置的保持，
# 并不要求数据项依次存放在连续的存储空间

class Node:
    def __init__(self, initdata) -> None:
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

# 可以采用连接节点的方式来构建数据集来实现无序表
# 链表的第一个和最后一个节点最重要
# 如果想访问到链表中所有的节点，就必须从第一个结点开始沿着连接遍历下去

# 无序表必须要有对第一个节点的引用信息
# 设立一个属性head，保存对第一个节点的引用空表的head为None

class UnorderedList:
    def __init__(self):
        self.head = None

