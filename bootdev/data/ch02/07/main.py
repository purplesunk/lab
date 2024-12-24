from stack import Stack


def is_balanced(input_str):
    stack = Stack()
    for ch in input_str:
        if ch == '(' or ch == ')':
            stack.push(ch)
    openings = 0
    while stack.peek() != None:
        if stack.pop() == '(':
            if openings == 0:
                return False
            else:
                openings -= 1
        else:
            openings += 1
    return openings == 0
