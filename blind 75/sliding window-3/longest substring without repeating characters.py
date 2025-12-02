s = "abcabcbb"
charset = set()
l = 0
res=0
for r in range(len(s)):
    while s[r] in charset:
        charset.remove(s[l])
        l+=1
        print(charset)
    charset.add(s[r])
    print(charset)
    res = max(res,r-l+1)