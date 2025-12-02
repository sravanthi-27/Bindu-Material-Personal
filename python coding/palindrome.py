a = "madam"
if a == a[::-1]:
    print("Palindrome")
else:
    print("not a palindrome") 

print("For neglecting spaces")
a = " madam"
a = a.lstrip()
print(a)
if a == a[::-1]:
    print("Palindrome")
else:
    print("not a palindrome") 


