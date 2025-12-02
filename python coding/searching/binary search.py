nums = [3,2,8,7,5]
nums.sort()
print(nums)
l = 0
r = len(nums)-1
target = 2
while l<=r: #if l>r that means there is no target element in the array
    mid = (l+r)//2
    if nums[mid]==target:
        print("found at",mid)
        break
    elif target<nums[mid]:
        r = mid-1
    else:
        l = mid+1

