s = "anagram"
t="nagaram"
di1,di2={},{}
if len(s)!=len(t):
    print(False)
else:
    for i in range(len(s)):
        val1 = s[i]
        if val1 not in di1:
            di1[val1]=1
        else:
            di1[val1]+=1
        val2=t[i]
        if val2 not in di2:
            di2[val2]=1
        else:
            di2[val2]+=1
    print(di1==di2)

