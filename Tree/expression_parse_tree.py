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

tree = buildParseTree(('(3+(4*5))'))
evaluate(tree)