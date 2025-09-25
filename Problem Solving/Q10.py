s = "Python is an amazing language"
N = 5

words = s.split()
word_list = []
for word in words:
    if len(word) > N:
        word_list.append(word)

print(word_list)