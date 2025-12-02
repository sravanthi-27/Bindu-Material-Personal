def is_operator(c):
    return c in "+-*/^"

def postfix_to_infix(postfix):
    stack = []

    for token in postfix:
        if token.isalnum():  # Operand
            stack.append(token)
        elif is_operator(token):
            # Pop top two operands
            op2 = stack.pop()
            op1 = stack.pop()
            # Add parentheses to preserve precedence
            new_expr = f"({op1}{token}{op2})"
            stack.append(new_expr)

    # Final result should be the only element
    return stack[0] if stack else "" #if we use stack ans returned in square brackets
postfix_expr = "ab+c*"
infix_expr = postfix_to_infix(postfix_expr)
print("Postfix:", postfix_expr)
print("Infix:", infix_expr)
