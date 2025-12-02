def anagram(s1,s2):
    di1,di2 = {},{}
    if len(s1)!=len(s2):
        return False
    else:
        for i in range(len(s1)):
            val1 = s1[i]
            val2 = s2[i]
            if val1 not in di1:
                di1[val1]=1
            else:
                di1[val1]+=1 
            if val2 not in di2:
                di2[val2] = 1
            else:
                di2[val2]+=1
        for i in di1:
            if i not in di2 or di1[i] != di2[i]:
                return False
        return True
    
s1 = "abcab"
s2 = "bbac"   
ans = anagram(s1,s2)
print(ans)
