words = ["apple", "bat", "dog", "elephant", "cat", "fish"]

# def func(word):
#     return len(word) > 4

func = lambda word : len(word) > 4

print(list(filter(func, words)))