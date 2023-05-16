# 表达式解析树求值
import operator
from buildParseTree import buildParseTree
def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, \
            '*':operator.mul, '/':operator.truediv}
    
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild() #downsize

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal() #基本结束条件

tree = buildParseTree(str((3+(4*5))))
print(evaluate(tree))

# 后序遍历解决表达式求值
def postordereval(tree):
    opers = {'+':operator.add, '-': operator.sub, \
             '*':operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None

    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()
print(postordereval(tree))