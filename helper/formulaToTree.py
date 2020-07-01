from globalvars import OPERATORS as OP


class BinaryTreeNode:
    def __init__(self, c):
        self.data = c
        self.isOperator = True if c in OP else False
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.stack = []

    def make_tree(self, formula):
        for x in formula:
            if x in OP:
                if x == '!':
                    node = BinaryTreeNode(x)
                    node.right = self.stack.pop()
                    self.stack.append(node)
                else:
                    node = BinaryTreeNode(x)
                    q = self.stack.pop()
                    p = self.stack.pop()
                    node.left = p
                    node.right = q
                    self.stack.append(node)
            else:
                node = BinaryTreeNode(x)
                self.stack.append(node)
        return self.stack[-1]

    def generate_expr(self, root: BinaryTreeNode):
        if not root:
            return ""
        else:
            if root.data in OP:
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
