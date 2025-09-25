import re
s = "Hello@123! Python_3"
ans = re.sub(r'[^A-Za-z]', "", s)
print(ans)