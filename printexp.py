# 采用中序遍历递归算法来生成全括号中缀表达式
# 左 根 右

import operator
from buildParseTree import buildParseTree

def printexp(tree):
    sVal = "" # 中缀表达式的形式
    if tree and tree.getLeftChild():
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    elif tree:
        sVal = printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild())

    return sVal

a = buildParseTree('( 3 + ( 4 * 5 ) )')
print(printexp(a))




