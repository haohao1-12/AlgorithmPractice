# 建立表达式解析树 
from pythonds import trees
from Tree.stack import Stack
def buildParseTree(fpexp):
    fplist = fpexp.split()
    # 创建单词列表
    pStack = Stack()
    eTree = trees.BinaryTree('') # 创建一个空的树
    pStack.push(eTree) # 当前节点入栈
    currentTree = eTree

    for i in fplist: #从左到右扫描全括号表达式的每一个单词
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree) # 老的当前节点入栈
            currentTree = currentTree.getLeftChild()
            # 当前节点下降到左子节点

        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent

        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        
        elif i == ')':
            currentTree = pStack.pop()
        
        else:
            raise ValueError
        
    return eTree



        



