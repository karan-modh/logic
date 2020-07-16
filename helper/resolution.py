from copy import deepcopy


def print_sentences(sentences):
    for sentence in sentences:
        if len(sentence) == 0:
            print("")
            continue
        pr_str = sentence[0]
        for i in range(1, len(sentence)):
            pr_str += "|" + sentence[i]
        print(pr_str)
    print("###############")


def resolution(sentences, mode):
    expressions = deepcopy(sentences)
    changed = True
    while changed:
        changed = False
        for i in range(len(expressions)):
            expr1 = expressions[i]
            for j in range(i + 1, len(expressions)):
                expr2 = expressions[j]
                if not expr1 or not expr2:
                    continue
                if len(expr1) == 1 and len(expr2) == 1:
                    if expr1[0] == '!' + expr2[0] or '!' + expr1[0] == expr2[0]:
                        if mode:
                            print("performed r", i + 1, " and r", j + 1)
                        return 1
                for x in expr1:
                    if len(x) == 1:
                        temp = '!' + x
                    else:
                        temp = x[0]

                    if temp in expr2:
                        if mode:
                            print("performed r", i + 1, " and r", j + 1)
                        expr1.remove(x)
                        expr2.remove(temp)
                        changed = True
                        expr = expr1 + expr2
                        expressions.append(expr)
                        if mode:
                            print_sentences(expressions)
                        break
    return resolve(sentences, mode)


def resolve(expressions, mode):
    sentences = deepcopy(expressions)
    changed = True
    while changed:
        changed = False
        for i in range(len(sentences)):
            if len(sentences[i]) == 1:
                temp = sentences[i][0]
                if len(temp) == 2:
                    var = temp[1]
                else:
                    var = "!" + temp
                for j in range(len(sentences)):
                    if var in sentences[j]:
                        sentences[j].remove(var)
                        if mode:
                            print("performed r", i + 1, " and r", j + 1)
                        changed = True
                        if len(sentences[j]) == 0:
                            return 1
                        if mode:
                            print_sentences(sentences)
                    else:
                        continue
    return 0
