n = 11
count = 0
for i in range(n+1):
    for j in range(n+1):
        if i==j:
            continue
        s = i*i + j*j 
        k = int(s**0.5)
        if k<= n and k*k == s and k!=i and k!=j:
            count+=1
print(count)