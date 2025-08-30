words = ["apple", "bat", "dog", "elephant", "cat", "fish"]

def func(word):
    return len(word)

print(list(map(func, words)))