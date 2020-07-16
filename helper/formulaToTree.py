from globalvars import OPERATORS


class BinaryTreeNode:
    def __init__(self, c):
        self.data = c
        self.isOperator = True if c in OPERATORS else False
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        pass

    def make_tree(self, formula):
        x = formula[0]
        if x in OPERATORS:
            if x == '!':
                node = BinaryTreeNode(x)
                node.right = self.make_tree(formula[1])
            else:
                node = BinaryTreeNode(x)
                p = self.make_tree(formula[1])
                q = self.make_tree(formula[2])
                node.left = p
                node.right = q
        else:
            node = BinaryTreeNode(x)
        return node

    def generate_expr(self, root: BinaryTreeNode):
        if not root:
            return ""
        else:
            if root.data in OPERATORS:
                result = ""
                # result += "("
                result += self.generate_expr(root.left)
                result += root.data
                result += self.generate_expr(root.right)
                # result += ")"
                return result
            else:
                return root.data

    def divide_tree(self, root: BinaryTreeNode):
        if not root:
            return []
        roots = []
        if root.data == '&':
            roots += self.divide_tree(root.left)
            roots += self.divide_tree(root.right)
            return roots
        else:
            return [root]
