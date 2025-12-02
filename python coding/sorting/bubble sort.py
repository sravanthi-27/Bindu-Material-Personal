#| Pass | List Status      | Explanation     |
#| ---- | ---------------- | --------------- |
#| 1    | \[3, 5, 8, 4, 2] | Swap 5 and 3    |
#|      | \[3, 5, 8, 4, 2] | 5 and 8 no swap |
#|      | \[3, 5, 4, 8, 2] | Swap 8 and 4    |
#|      | \[3, 5, 4, 2, 8] | Swap 8 and 2    |
#| 2    | \[3, 5, 4, 2, 8] | No swap 3 and 5 |
#|      | \[3, 4, 5, 2, 8] | Swap 5 and 4    |
#|      | \[3, 4, 2, 5, 8] | Swap 5 and 2    |
#|      | \[3, 4, 2, 5, 8] | No swap 5 and 8 |
#| 3    | \[3, 4, 2, 5, 8] | No swap 3 and 4 |
#|      | \[3, 2, 4, 5, 8] | Swap 4 and 2    |
#|      | \[3, 2, 4, 5, 8] | No swap 4 and 5 |
#|      | \[3, 2, 4, 5, 8] | No swap 5 and 8 |
#| 4    | \[2, 3, 4, 5, 8] | Swap 3 and 2    |
#|      | \[2, 3, 4, 5, 8] | No swap 3 and 4 |
#|      | \[2, 3, 4, 5, 8] | No swap 4 and 5 |
#|      | \[2, 3, 4, 5, 8] | No swap 5 and 8 |
nums = [3,5,8,4,2]
for i in range(len(nums)-1):#bcz we are comparing i and i+1 when it reaches last elements it returns index error ,what happens if we didnt use outer loop at all then it just swaps and when the higher value reaches at end then it stops if we write for i in range(2): then it will stop at [3,4,2,5,8] last two only get sorted so for all elements to be sorted we have to write len(nums)-1 and to have efficiency write -i
    for j in range(len(nums)-1-i):#to remove last sorted element
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1]=nums[j+1],nums[j]
print(nums) #complexity o(n^2)


#what about when the array is already sorted we canreduce complexity form 0(n^2) to o(n)
nums = ["b","a"]
for i in range(len(nums)-1):
    swapped = False
    for j in range(len(nums)-1-i):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
            swapped = True
    if not swapped:
        break
print(nums)