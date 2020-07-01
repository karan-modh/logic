from .formulaToTree import BinaryTreeNode


def remove_implications(root: BinaryTreeNode):
    if not root:
        return None
    elif root.data == '>':
        root.left = remove_implications(root.left)
        root.right = remove_implications(root.right)

        p = root.left
        new_node = BinaryTreeNode('!')
        root.left = new_node
        root.left.right = p
        root.data = '|'

        return root
    else:
        root.left = remove_implications(root.left)
        root.right = remove_implications(root.right)
        return root


def remove_equivalence(root: BinaryTreeNode):
    if not root:
        return None
    elif root.data == '=':
        root.left = remove_equivalence(root.left)
        root.right = remove_equivalence(root.right)

        root.data = '&'
        p = root.left
        q = root.right

        negate_q = BinaryTreeNode('!')
        negate_q.right = q
        negate_p = BinaryTreeNode('!')
        negate_p.right = p

        left_node = BinaryTreeNode('|')
        left_node.left = p
        left_node.right = negate_q

        right_node = BinaryTreeNode('|')
        right_node.left = q
        right_node.right = negate_p

        root.left = left_node
        root.right = right_node
        return root
    else:
        root.left = remove_equivalence(root.left)
        root.right = remove_equivalence(root.right)
        return root


def move_not_inwards(root: BinaryTreeNode):
    if not root:
        return None
    elif root.data == '!':
        root.right = move_not_inwards(root.right)

        if root.right.data == '!':
            p = root.right.right
            return p
        elif root.right.data == '|':
            root.data = '&'
        elif root.right.data == '&':
            root.data = '|'
        else:
            root.right = move_not_inwards(root.right)
            return root

        p = root.right.left
        q = root.right.right

        negate_p = BinaryTreeNode('!')
        negate_p.right = p
        negate_q = BinaryTreeNode('!')
        negate_q.right = q

        root.right = negate_q
        root.left = negate_p

        root.left = move_not_inwards(root.left)
        root.right = move_not_inwards(root.right)
        return root
    else:
        root.left = move_not_inwards(root.left)
        root.right = move_not_inwards(root.right)
        return root


def spread_or_over_and(root: BinaryTreeNode):
    if not root:
        return None
    elif root.data == '|':
        if root.left.data == '&':
            r = root.right
            p = root.left.left
            q = root.left.right

        elif root.right.data == '&':
            r = root.left
            p = root.right.left
            q = root.right.right
        else:
            root.left = spread_or_over_and(root.left)
            root.right = spread_or_over_and(root.right)
            return root

        root.data = '&'
        left_node = BinaryTreeNode('|')
        left_node.left = p
        left_node.right = r

        right_node = BinaryTreeNode('|')
        right_node.left = q
        right_node.right = r

        root.left = left_node
        root.right = right_node

        root.left = spread_or_over_and(root.left)
        root.right = spread_or_over_and(root.right)
        return root
    else:
        root.left = spread_or_over_and(root.left)
        root.right = spread_or_over_and(root.right)
        return root
