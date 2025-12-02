n = 43261596

a = bin(n)[2:].zfill(32)   # remove '0b' and pad to 32 bits
b = a[::-1]                # reverse exactly 32 bits
num = int(b, 2)            # convert back to int

print(num)
