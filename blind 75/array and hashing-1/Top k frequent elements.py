nums = [1,1,1,2,2,3]
k = 2
res = []
di = {}
for i in range(len(nums)):
    val = nums[i]
    if val not in di:
        di[val]=1
    else:
        di[val]+=1
frequecy = list(di.items())
frequecy.sort(key=lambda x:x[1],reverse=True)
for i in range(k):
    res.append(frequecy[i][0])
print(res)

#optimal
res1=[]
count = {}
freq = [[] for i in range(len(nums)+1)]
for n in nums:
    count[n] =  1+count.get(n,0)
for n,c in count.items():
    freq[c].append(n)
res = []
for i in range(len(freq)-1,0,-1):
    for n in freq[i]:
        res1.append(n)
        if len(res1)==k:
            print(res1,freq)
