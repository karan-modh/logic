from globalvars import PARENTHESIS, OPERATORS


def parse(sentence):
    expressions = []
    operators = []
    i = 0
    while i < len(sentence):
        if sentence[i] == '!':
            if sentence[i+1] == '(':
                i += 2
                sub_str = ''
                count = 1
                while count != 0:
                    if sentence[i] == '(':
                        count += 1
                    elif sentence[i] == ')':
                        count -= 1
                    if count > 0:
                        sub_str += sentence[i]
                    i += 1
                expressions.append(['!', parse(sub_str)])
            else:
                expressions.append(['!', sentence[i+1]])
                i += 2

        elif sentence[i] not in PARENTHESIS and sentence[i] not in OPERATORS:
            expressions.append(sentence[i])
            i += 1

        elif sentence[i] in OPERATORS:
            operators.append(sentence[i])
            i += 1

        elif sentence[i] == '(':
            i += 1
            sub_str = ''
            count = 1
            while count != 0:
                if sentence[i] == '(':
                    count += 1
                elif sentence[i] == ')':
                    count -= 1
                if count > 0:
                    sub_str += sentence[i]
                i += 1
            expressions.append(parse(sub_str))

    while operators:
        operand1 = expressions.pop()
        operand2 = expressions.pop()
        operator = operators.pop()
        expressions.append([operator, operand2, operand1])

    if len(expressions) == 1:
        return expressions[0]
    return expressions
