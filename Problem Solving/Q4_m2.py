s = "Hello@123! Python_3"

new_str = ""
for ch in s:
    if ch.isalpha():
        new_str = new_str + ch

print(new_str)
