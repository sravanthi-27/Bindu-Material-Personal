def is_operator(c):
    return c in "+-*/^"

def prefix_to_postfix(prefix):
    stack = []

    # Process the expression from right to left
    for token in reversed(prefix):
        if token.isalnum():  # Operand
            stack.append(token)
        elif is_operator(token):
            op1 = stack.pop()
            op2 = stack.pop()
            expr = op1 + op2 + token
            stack.append(expr)

    return stack[0] if stack else ""
prefix_expr = "*+abc"
postfix_expr = prefix_to_postfix(prefix_expr)

print("Prefix :", prefix_expr)
print("Postfix:", postfix_expr)
