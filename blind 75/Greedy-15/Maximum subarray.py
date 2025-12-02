nums = [-2,1,-3,4,-1,2,1,-5,4]
max_so_far = nums[0]
curr_max= nums[0]
for i in range(1,len(nums)):
    max_so_far = max(nums[i],nums[i]+max_so_far)
    curr_max = max(curr_max,max_so_far)
print(curr_max)