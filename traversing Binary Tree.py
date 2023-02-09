# 树的三种遍历

# 前序遍历

def preorder(tree):
    # 基本结束条件是该树为空树
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild()) # 递归访问左子树
        preorder(tree.getRightChild())

# 后序遍历 -- 左子树，右子树，根节点

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

# 中序遍历 -- 左子树， 根节点， 右子树

def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

