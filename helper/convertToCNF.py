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


def convert_to_cnf(sentences):
    sentence_trees = []
    modified_sentences = []
    for i in range(len(sentences)):
        temp_string = sentences[i]
        temp_string = in_to_post(temp_string)
        # print("PostFix form : ", temp_string)
        expr_tree = BinaryTree()
        root = expr_tree.make_tree(temp_string)
        root = convert_to_nnf(root)
        root = simplify(root)
        roots = expr_tree.divide_tree(root)
        for root in roots:
            modified_sentences.append(expr_tree.generate_expr(root))
        sentence_trees.append(root)
    return sentence_trees, modified_sentences
