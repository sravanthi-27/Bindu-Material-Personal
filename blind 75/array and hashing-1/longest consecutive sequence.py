nums = [1,0,1,2]
nums=set(nums)
nums=sorted(nums)
curr_len=1
max_len=1
if not nums:
    print(0)
for i in range(1,len(nums)):
    if nums[i]==1+nums[i-1]:
        curr_len+=1
    else:
        curr_len=1
    max_len = max(max_len,curr_len)
print(max_len,nums)

#optimal
nums = [100,4,200,1,3,2]
set_nums= set(nums)
longest = 0
for n in nums:
    #check if it is start of a sequence
    if n-1 not in set_nums:
        length = 0
        while n+length in set_nums:
            length+=1
        longest = max(length,longest)
print(longest)


