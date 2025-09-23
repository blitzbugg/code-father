def compress_string(s):
    if not s:
        return ""
    
    compressed = ""
    count = 1
    
    for i in range(len(s)):
        if i+1 < len(s) and s[i] == s[i+1]:
            count += 1
        else:
            compressed += s[i] + str(count)
            count = 1
    
    return compressed
 print(compress_string("aabcccccaaa"))  # Expected: "a2b1c5a3"