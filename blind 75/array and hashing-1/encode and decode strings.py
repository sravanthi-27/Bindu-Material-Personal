strs = ["neet", "code", "love", "you"]

# Encoder
def encode(strs):
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res

# Decoder
def decode(s):
    res = []
    i = 0
    while i < len(s):
        j = i
        # Find the position of '#'
        while s[j] != '#':
            j += 1
        length = int(s[i:j])         # get the length of the word
        word_start = j + 1
        word_end = j + 1 + length
        word = s[word_start:word_end]
        res.append(word)
        i = word_end
    return res

# Use like this:
encoded = encode(strs)
print("Encoded:", encoded)
decoded = decode(encoded)
print("Decoded:", decoded)
