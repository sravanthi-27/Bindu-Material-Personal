s = "()[]{}"
while "()" in s or "{}" in s or "[]" in s:
    s = s.replace("{}","")
    s = s.replace("[]","")
    s = s.replace("()","")
print(s=="")

#optimal
class Solution:
    def isValid(self, s: str) -> bool:
        #while '()' in s or '{}' in s or '[]' in s:
        #    s = s.replace('()', '').replace('{}', '').replace('[]', '')
        #if s == '':
        #    return True
        #else:
        #    return False
        stack = []
    
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            else:
                if not stack or stack.pop() != char:
                    return False
    
        return not stack #return True if stack is empty
    
solution = Solution()
print(solution.isValid(s))