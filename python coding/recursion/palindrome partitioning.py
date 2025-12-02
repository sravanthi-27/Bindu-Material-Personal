def is_palindrome(s):
    return s == s[::-1]

def partition_palindromes(s):
    result = []

    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])  # Add a copy of the current path
            return
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()  # Backtrack

    backtrack(0, [])
    return result
s = "aab"
print(partition_palindromes(s))
