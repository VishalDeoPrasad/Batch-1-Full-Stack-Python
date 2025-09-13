def is_palindrome(s):
    s = s.lower()
    rev_s = s[::-1]
    return s == rev_s

def reverse_string(s):
    return s[::-1]
