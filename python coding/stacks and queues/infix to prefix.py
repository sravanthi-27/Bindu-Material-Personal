def precedence(op):
    if op == '^':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    else:
        return 0

def is_operand(char):
    return char.isalnum()

def infix_to_postfix(expr):
    stack = []
    output = []

    for token in expr:
        if is_operand(token):
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '('
        else:
            while (stack and precedence(stack[-1]) > precedence(token)
                   and token != '^'):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

def infix_to_prefix(expression):
    # Step 1: Reverse the expression
    reversed_expr = expression[::-1]

    # Step 2: Swap ( and )
    swapped = []
    for ch in reversed_expr:
        if ch == '(':
            swapped.append(')')
        elif ch == ')':
            swapped.append('(')
        else:
            swapped.append(ch)

    # Step 3: Infix to postfix of modified expression
    postfix = infix_to_postfix(swapped)

    # Step 4: Reverse postfix to get prefix
    return postfix[::-1]
expr = "(a+b)*c-d+f"
prefix = infix_to_prefix(expr)
print("Prefix:", prefix)
