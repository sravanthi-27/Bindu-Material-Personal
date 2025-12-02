s = "ABABBA"
count = {}
res = 0
l = 0
k=2
for r in range(len(s)):
    count[s[r]] = 1+count.get(s[r],0)
    while (r-l+1)-max(count.values())>k:
        count[s[l]]-=1
        l+=1
    res = max(res,r-l+1)
print(res,count)

#optimal
s = "ABABBA"
count = {}
res = 0
l = 0
k=2
maxfreq = 0
for r in range(len(s)):
    count[s[r]] = 1+count.get(s[r],0)
    maxfreq = max(maxfreq,count[s[r]])
    while (r-l+1)-maxfreq>k:
        count[s[l]]-=1
        l+=1
    res = max(res,r-l+1)
print(res)