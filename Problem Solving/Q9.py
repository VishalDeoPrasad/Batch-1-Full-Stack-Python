s = "The quick brown fox jumps over a lazy dog"

s = s.lower()

unique_char = set()
for ch in s:
    if ch.isalpha():
        unique_char.add(ch)

if len(unique_char) == 26:
    print(True)
else:
    print(False)
