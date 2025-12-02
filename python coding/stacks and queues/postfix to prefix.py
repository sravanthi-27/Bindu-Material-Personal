def is_operator(c):
    return c in "+-*/^"

def postfix_to_prefix(postfix):
    stack = []

    for token in postfix:
        if token.isalnum():  # Operand
            stack.append(token)
        elif is_operator(token):
            op2 = stack.pop()
            op1 = stack.pop()
            expr = token + op1 + op2
            stack.append(expr)

    return stack[0] if stack else ""
postfix_expr = "ab+c*"
prefix_expr = postfix_to_prefix(postfix_expr)

print("Postfix:", postfix_expr)
print("Prefix :", prefix_expr)
