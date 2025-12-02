s = "A man, a plan, a canal: Panama"
s=s.lower()
res=""
for i in range(len(s)):
    if s[i].isalnum():
        res+=s[i]
print(res)
print(res==res[::-1])

#list comprehension->a = ''.join([char for char in s if char.isalnum()])

#not using alnum,space:O(1)


s1 = "A man, a plan, a canal: Panama"

def palindrome(s):
    l,r = 0,len(s1)-1
    while l<r:
        while l<r and not alphanums(s1[l]):
            l+=1
        while r>l and not alphanums(s1[r]):
            r-=1
        if s1[l].lower()!=s1[r].lower():
            return False
        l+=1
        r-=1
    return True
def alphanums(c):
    return (ord('A')<=ord(c)<=ord('Z')) or (ord("a")<=ord(c)<=ord("z")) or (ord("0")<=ord(c)<=ord("9"))
print(palindrome(s1))