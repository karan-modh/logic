from globalvars import VARIABLES


class Conversion:

    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.stack = []
        self.output = []

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.stack[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.stack.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.stack.append(op)

    def isVariable(self, ch):
        return True if ch in VARIABLES else False

    def infixToPostFix(self, exp):
        skipped = False
        for j in range(len(exp)):
            if skipped:
                skipped = False
                continue
            i = exp[j]
            if self.isVariable(i):
                self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while not self.isEmpty() and self.peek() != '(':
                    a = self.pop()
                    self.output.append(a)
                    if not self.isEmpty() and self.peek() != '(' and a != '!':
                        return -1
                    elif a == '!':
                        if self.peek() == '(':
                            self.pop()
                        else:
                            pass
                    else:
                        self.pop()
            elif i == '!' and self.isVariable(exp[j+1]):
                self.output.append(exp[j+1])
                self.output.append(i)
                skipped = True
            else:
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())

        return "".join(self.output)
