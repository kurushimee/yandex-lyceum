def palindrome(s):
    s = s.lower().split()
    s = "".join(s)
    n = "".join(s)[::-1]
    if n == s:
        return "Палиндром"
    return "Не палиндром"
