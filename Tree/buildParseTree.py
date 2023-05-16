# 建立表达式解析树 
from BinaryTree_class import BinaryTree
from stack import Stack
def buildParseTree(fpexp):
    fplist = fpexp.split()
    # 创建单词列表
    pStack = Stack()
    eTree = BinaryTree('') # 创建一个空的树
    pStack.push(eTree) # 当前节点入栈
    currentTree = eTree

    for i in fplist: #从左到右扫描全括号表达式的每一个单词
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree) # 老的当前节点入栈
            currentTree = currentTree.getLeftChild()
            # 当前节点下降到左子节点

        elif i not in '+-*/)':
            currentTree.setRootVal(eval(i))
            parent = pStack.pop()
            currentTree = parent

        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        
        elif i == ')':
            currentTree = pStack.pop()
        
        else:
            raise ValueError
        
    return eTree


# 生成全括号中缀表达式 (左根右)
# 用表达式解析树恢复表达式字符串形式
def printexp(tree):
    sVal = ""
    if tree:
        sVal = '(' + str(printexp(tree.getLeftChild()))
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + str(printexp(tree.getRightChild()))+ ')'
    return sVal
    
tree = buildParseTree('(3+(4*5))')
print(tree.getLeftChild())
        



