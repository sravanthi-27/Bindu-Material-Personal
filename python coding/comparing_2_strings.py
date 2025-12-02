print("For case insensitive")
a = "mAdAm"
b = "MaDaM"
for i,j in zip(a,b):
    if ord(i)-ord(j) == -(ord(j)-ord(i)):    # or converting both into lowercase
        print("palindrome")
    else:
        print("No")
