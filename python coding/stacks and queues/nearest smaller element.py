def nearest_smaller_element(arr):
    n = len(arr)
    stack = []
    result = [-1]*n
    for i in range(len(arr)):
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result 
ans = nearest_smaller_element([4,5,2,10,8])
print(ans)
