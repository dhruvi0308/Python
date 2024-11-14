def is_palindrome(s):
    
    return s == s[::-1]
strings = ["radar", "hello", "level", "world"]

for s in strings:
    result = is_palindrome(s)
    print(f"'{s}' is a palindrome: {result}")
