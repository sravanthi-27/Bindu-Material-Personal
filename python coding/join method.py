'''s = "ADOBECODEBANC"
t = "ABC"
l= 0
ans = []
if len(t)<len(s):
    for r in range(len(s)):
        while s[r] in t:
            ans.append(s[r])
        else:
            if ans:
                del ans[l]
#ans = ''.join(ans)
print(ans)'''