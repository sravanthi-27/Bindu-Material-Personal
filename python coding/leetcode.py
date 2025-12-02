''' sqrt
from itertools import count
x = int(input())
for i in count(0):
    a = x**(1/2)
    a = int(a)
    if i == a:
        print(i)
        break
    else:
        i+=1
'''

'''returns unique element
a = [1,2,1,2,3]
for i in range(len(a)):
    b = a.count(a[i])
    if b == 1:
        print(a[i])'''

'''palindrome
s = "123321"
a = ''.join([char for char in s if char.isalnum()])
a = a.lower()
print(a)
if a == a[::-1]:
     print("S")
else:
    print("N")'''

'''add one to list and return list
digits = [1,2,3]
for i in range(len(digits)):
    digits[i] = str(digits[i])
print(digits)
a = ''.join(digit for digit in digits)
a = int(a)
a = a+1
c = [int(c) for c in str(a)]
print(c)'''

'''removing duplicate node from a lis
l = [1,1,2,3]
b = []
count = 1
for i in range(len(l)):
    a = l.count(l[i])
    if a>1:
       b.append(l[i]) 
for i in range(len(b)):
    a = l.remove(b[i])
    print(l)  '''

'''removing duplicate node from a listnode/linkedlist
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head  # Start from the head node

        while current and current.next:
            if current.val == current.next.val:  
                current.next = current.next.next  # Skip the duplicate node
            else:
                current = current.next  # Move to the next unique node

        return head  # Return the modified linked list
'''      

'''happy number
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set() #for n=14 (maximum recursion depth)
        while n not in seen:  # ✅ Loop to track cycles instead of recursion depth error
            if n == 1 or n == 7:
                return True
            seen.add(n)  # ✅ Store visited numbers
            
            digits = [int(d) for d in str(n)]
            e = sum(d**2 for d in digits)
            if e == 1:
                return True
            else:
                n = e  # ✅ Update n instead of recursive call
        
        return False  # ✅ If a cycle is detected, return False                       }'''

'''valid paranthesis
class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        if s == '':
            return True
        else:
            return False''' 

'''add binary
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b= int(a,2),int(b,2)
        c = a+b
        print(bin(c)[2:])
solution = Solution()
solution.addBinary("11","1")'''

'''substring index in string
haystack = "sadbutsad"
needle = "sad"
if needle in haystack:
    a = haystack.index(needle)
    print(a)
else:
    print("false")'''

'''length of last word in a string
s = "   fly me   to   the moon  "
a = s.strip()
a = a.split(" ")
print(a)
print(len(a[-1]))'''

'''longest substring
def common_substring(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for word in strings[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]  #removes last character from prefix
            if not prefix:  #empty prefix
                return ""
    return prefix
# Example usage
strings = ["flower","flow","flight"]
print(common_substring(strings))  '''

'''roman to integer
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev = 0
        
        for char in reversed(s):  # Iterate from the right
            curr = roman[char]
            if curr < prev:  
                total -= curr  # Subtract if a smaller numeral comes before a larger one
            else:
                total += curr
            prev = curr  # Update previous value
        
        return total

# Example usage
solution = Solution()
print(solution.romanToInt("IX"))   # Output: 9
print(solution.romanToInt("LVIII")) # Output: 58
print(solution.romanToInt("MCMXCIV")) # Output: 1994'''

'''from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Dummy node to start the merged list
        current = dummy     # Pointer to build the list

        # Merge both lists while they have elements
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If any nodes are left in either list, attach them
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next  # Return the head of the merged sorted list'''
'''climbing stairs
method1
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        else:
            solution = Solution()
            a = solution.climbStairs(n-1)
            b = solution.climbStairs(n-2)
            return a + b
a = [1,2,3]
for i in range(2,46):
    solution = Solution()
    b =a.append(solution.climbStairs(i))
print(a)

method2
num = int(input())
a = [1,1]
for i in range(2,num):
    c = a[i-1] + a[i-2]
    a.append(c)
print(a)
print(a[-1] + a[-2])'''

'''appending list2 in list1
nums1 = [1,2,3]
nums2 = [2,5,6]
m = len(nums1)
n = len(nums2)
for i in range(len(nums2)):
    nums1.append(nums2[i])
nums1.sort()
print(nums1)'''

'''adding list2 in list1
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = len(nums1)
n = len(nums2)
for i in range(-1, -(n+1), -1):
    nums1[i] += nums2[i]
a = nums1.sort()
print(nums1)'''

'''a = [1,1]
sum = 0
b = [1,1]
for i in range(len(a)):
     sum = sum+a[i]
     print(sum)
b.insert(1,sum)
print(b)'''

'''majority element by count method1:
a = [2,2,1,1,1,2,2]
a = tuple(a)
b = []
for i in range(len(a)):
    c = a.count(a[i])
    b.append(c)
    c = max(b)
for i in range(len(a)):
    if c == a.count(a[i]):
        print(a[i])
        break 

method2:
from collections import Counter
a = [3, 3, 4]
freq = Counter(a)  # Creates a dictionary {element: frequency}
print(freq)  # Output: Counter({3: 2, 4: 1})
key = max(freq, key=freq.get)  # Finds the key with the max count
print(key)  # Output: 3'''

'''class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Counter for elements not equal to val
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k       Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.'''

'''from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):  # Corrected range
            if target == nums[i]:  
                return i  # Return index if found
            elif target < nums[i]:  
                return i  # Return insert position if target is smaller
        return len(nums)  # If target is larger than all elements, insert at the end'''

'''remove duplicates from sorted array -class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # If empty list, return 0
        
        unique_index = 0  # Start with the first element
        
        for i in range(1, len(nums)):  # Loop from the second element
            if nums[i] != nums[unique_index]:  # If different from last unique
                unique_index += 1  # Move pointer
                nums[unique_index] = nums[i]  # Update array with unique value
        
        return unique_index + 1  # Return number of unique elements'''

'''2sums:nums = list(map(int, input("Enter the numbers separated by space: ").split()))
target = int(input("Enter the target sum: "))
 for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j]== target:
                    return [i, j]
        # Return an empty list if no solution is found
        return []'''

'''palindrome:class Solution:
    def isPalindrome(self, x: int) -> bool:               ++++*++++          4
        x = str(x)                                        +++***+++         345     
        return x == x[::-1]                               ++*****++        23456
                                                          +******++       1234567
                                                          *********      0123456789
        
        '''
'''r = 10
n = r-1
for i in range(r):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(i*2+1):
        print("*",end=" ")
    print()'''

'''def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    mid = (low+high)//2
    print(low,high,mid)
    if arr[mid] == target:
        print("found",mid)
    elif arr[mid]<target:
        high = mid-1
        binary_search(arr[low:high+1],target)
    elif arr[mid]>target:
        low = mid+1
        binary_search(arr[low:],target)
    else:
        print("not found")
binary_search([1,2,3,4,5],3)'''

'''nums = [3,2,3,4,6,5]
result = []
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]==nums[j]:
            result.append(nums[i])
            new = nums[i]-1
            new1 = nums[i]+1
            if new in nums or new==0:
                result.append(new1)
            else:
                result.append(new)
print(result)'''

'''s = "xyzzaz"
l = 0
k = 3
result = []
strings=""
for r in range(len(s)):
    strings+=s[r]
    if r-l+1==k:
        result.append(strings)
        strings=s[l+1:]
        l+=1
print(result)'''

'''arr = [["a1",0,6],["a2",3,4],["a3",1,2],["a4",5,9],["a5",5,7],["a6",8,9]]
arr.sort(key=lambda x:(x[2]))
ans = 1 
index = 0     
res = [arr[0][0]]
#print(res,ans,arr)
for i in range(1,len(arr)):
    if arr[i][1] >= arr[index][2]:
        index = i 
        ans+=1
        res.append(arr[i][0])
print(res,ans)'''
'''if ratings[i]>ratings[i-1]:
        res[i]+=1
    if ratings[i]>ratings[i+1]:
        res[i]+=1'''

'''class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        # Store array elements in set for O(1) lookup
        num_set = set(arr)
        max_len = 0
        n = len(arr)
#arr = [1, 3, 7, 11, 12, 14, 18]
        # Try all possible first two numbers of sequence
        for start in range(n):
            for next in range(start + 1, n):
                # Start with first two numbers
                prev = arr[next]
                curr = arr[start] + arr[next]
                curr_len = 2

                # Keep finding next Fibonacci number
                while curr in num_set:
                    prev, curr = curr, curr + prev
                    curr_len += 1
                    max_len = max(max_len, curr_len)

        return max_len'''


