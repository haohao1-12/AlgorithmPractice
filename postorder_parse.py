import operator
from buildParseTree import buildParseTree

def postorderval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    res1 = None
    res2 = None

    if tree:
         res1 = postorderval(tree.getLeftChild())
         res2 = postorderval(tree.getRightChild())

         if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
         else:
            return tree.getRootVal()

a = buildParseTree('( 3 + ( 4 * 5 ) )')
print(postorderval(a))