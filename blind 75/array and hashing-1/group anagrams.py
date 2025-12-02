strs = ["eat","tea","tan","ate","nat","bat"]
groups = {}
for s in strs:
    sorted_str = ''.join(sorted(s))
    if sorted_str not in groups:
        groups[sorted_str]=[]
    groups[sorted_str].append(s)


print(list(groups.values()))

#optimal
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)  #if you want integer di = defaultdict(int)   int() returns 0 by default ,if you want integer 1 use di = defaultdict(lambda: 1)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
sol = Solution()
input_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = sol.groupAnagrams(input_list)
print(result)

d = {}
key = (1, 0, 0)
d[key] = "value"  # ❌ TypeError: unhashable type: 'list' in dictionaries we cant use list as keys so convert into tuple and then use
print(d)