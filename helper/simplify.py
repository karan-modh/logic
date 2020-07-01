from .formulaToTree import BinaryTreeNode
from globalvars import OPERATORS


def is_equal(left_root: BinaryTreeNode, right_root: BinaryTreeNode):
    if left_root and right_root:
        if left_root.data != right_root.data:
            return False
        return is_equal(left_root.left, right_root.left) and is_equal(left_root.right, right_root.right)
    elif not left_root and not right_root:
        return True
    else:
        return False


def remove_true_terms(root: BinaryTreeNode):
    if not root:
        return None
    elif root.data == '&':
        if is_equal(root.left, root.right):
            return None
        else:
            root.left = remove_true_terms(root.left)
            root.right = remove_true_terms(root.right)
            return root
    elif root.data == '|':
        if is_equal(root.left, root.right):
            return None
        elif root.left.data == '!' and is_equal(root.left.right, root.right):
            return None
        elif root.right.data == '!' and is_equal(root.right.right, root.left):
            return None
        else:
            root.left = remove_true_terms(root.left)
            root.right = remove_true_terms(root.right)
            return root
    else:
        root.left = remove_true_terms(root.left)
        root.right = remove_true_terms(root.right)
        return root


def remove_unused_ops(root: BinaryTreeNode):
    if not root:
        return None
    if not root.left or not root.right:
        if root.data == '!':
            root.right = remove_unused_ops(root.right)
            return root
        elif root.data in OPERATORS:
            if not root.left:
                root.right = remove_unused_ops(root.right)
                temp = root.right
            elif not root.right:
                root.left = remove_unused_ops(root.left)
                temp = root.left
            else:
                return None
            root.data = temp.data
            root.left = temp.left
            root.right = temp.right
            return root
        else:
            root.right = remove_unused_ops(root.right)
            root.left = remove_unused_ops(root.left)
            return root
    else:
        root.right = remove_unused_ops(root.right)
        root.left = remove_unused_ops(root.left)
        return root
