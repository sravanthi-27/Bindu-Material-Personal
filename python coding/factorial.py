def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

print("Without using recursive function")
n = int(input())
a = 1
for i in range(1,n+1):
    a = a*i
print(a)

print("using while loop")
# cook your dish here
def factorial(n):
    factorial = 1
    while n>1:
        factorial *= n 
        n -=1
    return factorial