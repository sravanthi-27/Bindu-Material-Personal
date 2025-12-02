'''n,c,m = 6,2,2
wrapper = n//c 
result = wrapper
#print(wrapper)
if wrapper>=m:
    result_wrappers = wrapper//m 
    result += result_wrappers
print(result)'''

'''n = 5
for i in range(0,2*n):
    if i>n:
        cols = 2*n-i
    else:
        cols = i 
    for j in range(cols):
        print("*",end=" ")
    print()'''

'''n=5
for i in range(1,n+1):
    print("  "*(n-i)+" *"*i,end = "")
    print()'''

'''n=5
for i in range(n):
    print("* "*(n-i))'''

'''n = 5
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end = " ")
    print()'''
'''n=5
for i in range(n,0,-1):
    print(" "*(n-i)+"*"*(2*i-1))'''

check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
check2 = check1
check3 = check1[:]
check2[0] = 'Code'
check3[1] = 'Mcq'
count = 0
for c in (check1, check2, check3):
    if c[0] == 'Code':
        count += 1
    if c[1] == 'Mcq':
        count += 10

text = "Python"  
print(text[::-1])

fruits = ["apple", "banana", "cherry"]  
fruits.insert(3, "orange")  
print(fruits[3])  

def func():  
    pass  
print(func() )  

x = "Python"  
print(x.reverse())  
