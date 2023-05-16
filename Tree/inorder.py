# 生成全括号中缀表达式 (左根右)
# 用表达式解析树恢复表达式字符串形式
def printexp(tree):
    sVal = ""
    if tree:
        if isinstance(tree.getLeftChild(),int):
            sVal = printexp(tree.getLeftChild())
        else:
            sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        if isinstance(tree.getRightChild(),int):
            sVal = sVal + printexp(tree.getRightChild())
        else:
            sVal = sVal + printexp(tree.getRightChild())+ ')'
        return sVal
