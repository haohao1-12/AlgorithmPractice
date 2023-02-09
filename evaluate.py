import operator
from buildParseTree import buildParseTree

a = buildParseTree('( 3 + ( 4 * 5 ) )')

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*': operator.mul, '/': operator.truediv}

    # 缩小规模
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))

    else:
        return parseTree.getRootVal()


print(evaluate(a))

