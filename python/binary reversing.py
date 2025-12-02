#n = 00000010100101000001111010011100 
#this is not a way to represent binary numbers bcz python will throw error if its starting with more than one zero so use
n = 0b00000010100101000001111010011100  # ✅ valid binary literal
#add 0b in front of n
binary = format(n, '032b') #Converts it to 32-bit binary
reversed_binary = binary[::-1]
reversed_int = int(reversed_binary, 2) #2 is bcz we are converting binary number(base2) into an integer otherwise If you didn't use 2, Python would assume it's base 10 and throw an error if the string contains anything other than digits 0–9.