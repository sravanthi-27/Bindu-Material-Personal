def is_operator(c):
    return c in "+-*/^"

def prefix_to_infix(prefix):
    stack = []

    # Process from right to left
    for token in reversed(prefix):
        if token.isalnum():  # Operand
            stack.append(token)
        elif is_operator(token):
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = f"({op1}{token}{op2})"
            stack.append(new_expr)

    return stack[0] if stack else ""
prefix_expr = "*+ab-cd"
infix_expr = prefix_to_infix(prefix_expr)
print("Prefix:", prefix_expr)
print("Infix:", infix_expr)
