#!
def next_greater_element(arr): #looks right of the array
    n = len(arr)
    result = [-1]*n
    stack = []
    for i in range(n-1,-1,-1):
        while stack and stack[-1]<=arr[i]:
            stack.pop()
        if stack:
            result[i] = stack[-1]
        stack.append(arr[i])
    return result
arr = [4, 5, 2, 10, 8]
#print(next_greater_element(arr))  # Output: [5, 10, 10, -1, -1]


#2 next graeter element not only consider right bbut also circular 
def next_greater_element2(arr):
    n = len(arr)
    result = [-1]*n 
    stack = []
    for i in range(2*n-1,-1,-1):
        while stack and stack[-1]<=arr[i%n]:
            stack.pop()
        if stack:
            result[i%n] = stack[-1]
        stack.append(arr[i%n])
    return result 
ans = next_greater_element2([1,2,3,4,3])
print(ans)

#for two arrays leetcode:496
def nextGreaterElement(nums1, nums2):
    stack = [] #stores which doesnt have any greater element
    next_greater = {} #stores the gratest number

    for num in nums2:
        while stack and num > stack[-1]:
            last = stack.pop()
            next_greater[last] = num
        stack.append(num) 

    # For elements that have no next greater
    for num in stack:
        next_greater[num] = -1

    # Build the result for nums1 using the dictionary
    result = []
    for num in nums1:
        result.append(next_greater[num])

    return result
res = nextGreaterElement([4,1,2],[1,3,4,2])
print(res) #Time:O(n+m) n for nums2,m for nums1
#space:O(n+m) n for stack,n for dictionary,m for result list