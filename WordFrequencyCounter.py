def word_frequency(text):
    words = text.lower().split()
    freq = {}
    
    for word in words:
        word = word.strip('.,!?')
        freq[word] = freq.get(word, 0) + 1
    
    return freq
 print(word_frequency("Hello world, hello Python!"))
 # Expected: {'hello':2, 'world':1, 'python':1}