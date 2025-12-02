def get_permutation(n, k):
    # Step 1: prepare factorials and list of numbers
    factorial = [1] * (n +1) #We initialize with 1s: [1, 1, 1, 1] (for n = 3) the 1st element 0 index remains same after calculating factorials because factorial[0] =1 and for finding any factorial we need factorial[0]
    for i in range(1, n + 1): #fact[3] = 3! = 6 used for computing factorials
        factorial[i] = factorial[i - 1] * i

    nums = [str(i) for i in range(1, n + 1)] #nums = ['1', '2', '3']

    k -= 1  # convert to 0-based index
    result = []

    # Step 2: build the permutation
    for i in range(n, 0, -1):
        group_size = factorial[i - 1] #see book
        index = k // group_size
        result.append(nums[index])
        nums.pop(index)
        k %= group_size

    return ''.join(result)
print(get_permutation(4, 17))  # Output: "3412"
