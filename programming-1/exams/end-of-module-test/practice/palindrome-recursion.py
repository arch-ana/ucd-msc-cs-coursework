def palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])

a = palindrome("kayak")
b = palindrome('archana')
print(a)
print(b)