#brute force
nums = [1,2,-2,-1]
res = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                path = [nums[i],nums[j],nums[k]]
                path.sort()
                if path not in res:
                    res.append(path)
print(res)

#brute force2
res = []
nums = [-1,0,1,2,-1,-4]
for i in range(len(nums)):
    lis = []
    for j in range(i+1,len(nums)):
        third = -(nums[i]+nums[j])
        if third in lis:
            temp = [nums[i],nums[j],third]
            temp.sort()
            if temp not in res:
                res.append(temp)
        else:
            lis.append(nums[j])
print(res)

#optimal
nums = [0, 0, 0]
nums.sort()
res = []

for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue  # skip duplicate 'i'
    j, k = i + 1, len(nums) - 1

    while j < k:
        total = nums[i] + nums[j] + nums[k]

        if total == 0:
            res.append([nums[i], nums[j], nums[k]])
            # Skip duplicates for j and k
            while j < k and nums[j] == nums[j + 1]:
                j += 1
            while j < k and nums[k] == nums[k - 1]:
                k -= 1
            j += 1
            k -= 1
        elif total < 0:
            j += 1
        else:
            k -= 1

print(res)