# Function to define precedence
def precedence(op):
    if op == '^':
        return 3
    elif op in ('*', '/'):
        return 2
    elif op in ('+', '-'):
        return 1
    else:
        return 0

# Function to check if character is an operand
def is_operand(char):
    return char.isalnum()  # Handles variables and numbers

# Main function: infix to postfix
def infix_to_postfix(expression):
    stack = []         # Stack for operators
    output = []        # Result list for postfix

    for token in expression:
        if is_operand(token):
            output.append(token)  # Operand → goes directly to output

        elif token == '(':
            stack.append(token)   # Opening parenthesis → push to stack

        elif token == ')':
            # Pop until matching '('
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Discard '('

        else:
            # Operator: pop while precedence is >= current
            while (stack and precedence(stack[-1]) >= precedence(token)
                   and token != '^'):  # right-associative ^ exception
                output.append(stack.pop())
            stack.append(token)  # Push current operator  ,  Whenever you hit an operator like +, *, ^, etc., you push it onto the stack — but only after popping higher or equal precedence operators already on the stack.

    # Pop remaining operators
    while stack:
        output.append(stack.pop())

    return ''.join(output)
ans = infix_to_postfix("a+b*c")
print(ans)