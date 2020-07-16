from .inToPost import Conversion
from .formulaToTree import BinaryTree
from .ToNNF import remove_equivalence, remove_implications, move_not_inwards, spread_or_over_and
from .simplify import remove_true_terms, remove_unused_ops


def in_to_post(formula):
    obj = Conversion(len(formula))
    return obj.infixToPostFix(formula)


def convert_to_nnf(root):
    root = remove_implications(root)
    root = remove_equivalence(root)
    root = move_not_inwards(root)
    root = spread_or_over_and(root)
    return root


def simplify(root):
    root = remove_true_terms(root)
    root = remove_unused_ops(root)
    return root


def convert_to_cnf(expressions):
    modified_sentences = []
    for expression in expressions:
        expr_tree = BinaryTree()
        root = expr_tree.make_tree(expression)
        root = convert_to_nnf(root)
        root = simplify(root)
        roots = expr_tree.divide_tree(root)

        for root in roots:
            modified_sentences.append(expr_tree.generate_expr(root))

    return modified_sentences
